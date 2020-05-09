import logging
import os
import time

import requests

from jinx.exceptions import JinxAuthenticationError

logger = logging.getLogger(__name__)

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
    token: str, optional
        Authentication token (required for use with IEX Cloud)
    """

    _URLS = {
        "v1": "https://cloud.iexapis.com/v1/",
        "iexcloud-beta": "https://cloud.iexapis.com/v1/",
        "iexcloud-v1": "https://cloud.iexapis.com/v1/",
        "iexcloud-sandbox": "https://sandbox.iexapis.com/v1/",
    }

    _VALID_FORMATS = ("json", "pandas")
    _VALID_CLOUD_VERSIONS = ("iexcloud-beta", "iexcloud-v1",
                             "v1", "iexcloud-sandbox")


    def _init_session(session, retry_count=3):
        if session is None:
            session = requests.session()
        return session


    def __init__(self, **kwargs):
        self.retry_count = kwargs.get("retry_count", 3)
        self.pause = kwargs.get("pause", 0.5)
        self.session = self._init_session(kwargs.get("session"))
        self.json_parse_int = kwargs.get("json_parse_int")
        self.json_parse_float = kwargs.get("json_parse_float")
        self.token = kwargs.get("token")

        # Get desired API version from environment variables
        # Defaults to IEX Cloud
        self.version = os.getenv("IEX_API_VERSION", "v1")
        if self.version in self._VALID_CLOUD_VERSIONS:
            if self.token is None:
                self.token = os.getenv("IEX_TOKEN")
            if not self.token or not isinstance(self.token, str):
                raise JinxAuthenticationError(
                    "The IEX Cloud API key must be provided "
                    "either through the token variable or "
                    "through the environmental variable "
                    "IEX_TOKEN."
                )
        else:
            raise ValueError("Please select a valid API version.")
