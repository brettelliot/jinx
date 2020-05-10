import logging
import os
import time
import requests
from jinx.exceptions import JinxAuthenticationError
from jinx.exceptions import JinxQueryError
from jinx.exceptions import JinxSymbolError

log = logging.getLogger(__name__)

class _JinxBase(object):
    """
    Base class for retrieving equities information from IEX Cloud.
    Conducts query operations including preparing and executing queries from
    the API.

    Attributes
    ----------
    retry_count: int, default 3, optional
        Desired number of retries if a request fails
    pause: float default 0.5, optional
        Pause time between retry attempts
    session: requests_cache.session, default None, optional
        A cached requests-cache session
    json_parse_int: datatype, default int, optional
        Desired integer parsing datatype
    json_parse_float: datatype, default float, optional
        Desired floating point parsing datatype
    """

    _URLS = {
        "v1": "https://cloud.iexapis.com/v1/",
        "iexcloud-beta": "https://cloud.iexapis.com/v1/",
        "iexcloud-v1": "https://cloud.iexapis.com/v1/",
        "iexcloud-sandbox": "https://sandbox.iexapis.com/v1/",
    }

    _VALID_CLOUD_VERSIONS = ("iexcloud-beta", "iexcloud-v1",
                             "v1", "iexcloud-sandbox")

    def _init_session(self, session, retry_count=3):
        if session is None:
            session = requests.session()
        return session


    def __init__(self, **kwargs):
        self.retry_count = kwargs.get("retry_count", 3)
        self.pause = kwargs.get("pause", 0.5)
        self.session = self._init_session(kwargs.get("session"))
        self.json_parse_int = kwargs.get("json_parse_int")
        self.json_parse_float = kwargs.get("json_parse_float")
        self.token = os.getenv("IEX_TOKEN")

        # Get desired API version from environment variables
        # Defaults to IEX Cloud
        self.version = os.getenv("IEX_API_VERSION", "v1")
        if self.version in self._VALID_CLOUD_VERSIONS:
            if not self.token or not isinstance(self.token, str):
                raise JinxAuthenticationError(
                    "The IEX Cloud API key must be provided "
                    "either through the token variable or "
                    "through the environmental variable "
                    "IEX_TOKEN."
                )
        else:
            raise ValueError("Please select a valid API version.")

    def _validate_response(self, response):
        """ Ensures response from IEX server is valid.

        Parameters
        ----------
        response: requests.response
            A requests.response object

        Raises
        ------
        JinxSymbolError
            If a single Share symbol is invalid
        """
        # log the number of messages used
        key = "iexcloud-messages-used"
        if key in response.headers:
            msg = response.headers[key]
        else:
            msg = "N/A"
        log.info("MESSAGES USED: %s" % msg)

        if response.text == "Unknown symbol":
            raise JinxSymnbolError(response.status_code, response.text)

    def _execute_iex_text_request(self, path, params):
        """ Executes HTTP Request
        Given a path, execute HTTP request from IEX server. If request is
        unsuccessful, attempt is made self.retry_count times with pause of
        self.pause in between.

        Parameters
        ----------
        path: str
            A properly-formatted endpoint path suitable for being appended to
            an IEX base URL and version. For example: "/stock/AAPL/financials/"
        params: dict
            A dictionary of query params to be added to the endpoint path

        Returns
        -------
        text: str
            Content of requests.response.text

        Raises
        ------
        JinxQueryError
            If problems arise when making the query
        """
        url = self._URLS[self.version] + path
        params["token"] = self.token
        for _ in range(self.retry_count + 1):
            response = self.session.get(url=url, params=params)
            log.debug("REQUEST: %s" % response.request.url)
            log.debug("RESPONSE: %s" % response.status_code)
            if response.status_code == requests.codes.ok:
                self._validate_response(response)
                return response.text
            time.sleep(self.pause)
        return self._handle_error(response)

    def _execute_iex_json_request(self, path, params):
        """ Executes HTTP Request
        Given a path, execute HTTP request from IEX server. If request is
        unsuccessful, attempt is made self.retry_count times with pause of
        self.pause in between.

        Parameters
        ----------
        path: str
            A properly-formatted endpoint path suitable for being appended to
            an IEX base URL and version. For example: "/stock/AAPL/financials/"
        params: dict
            A dictionary of query params to be added to the endpoint path

        Returns
        -------
        json_respnose: dict
            Dictionary containing validate json from the response

        Raises
        ------
        JinxQueryError
            If problems arise when making the query
        """
        url = self._URLS[self.version] + path
        params["token"] = self.token
        for _ in range(self.retry_count + 1):
            response = self.session.get(url=url, params=params)
            log.debug("REQUEST: %s" % response.request.url)
            log.debug("RESPONSE: %s" % response.status_code)
            if response.status_code == requests.codes.ok:
                self._validate_response(response)
                try:
                    json_response = response.json(
                        parse_int=self.json_parse_int,
                        parse_float=self.json_parse_float)
                    if (isinstance(json_response, str) and
                            ("Error Message" in json_response)):
                        raise JinxQueryError(response.status_code,
                                            response.text)
                except ValueError:
                    raise JinxQueryError(response.status_code, response.text)
                return json_response
            time.sleep(self.pause)
        return self._handle_error(response)

    def _handle_error(self, response):
        """
        Handles all responses which return an error status code
        """
        raise JinxQueryError(response.status_code, response.text)
