import logging
import requests
from jinx.base import _JinxBase
from jinx.exceptions import JinxSymbolError

log = logging.getLogger(__name__)

class Stock(_JinxBase):
    """Base class for obtaining data abouot a stock from IEX.

    Attributes
    ----------
    symbol: str
        Ticker symbol
    """

    def __init__(self, symbol=None, **kwargs):
        super(Stock, self).__init__(**kwargs)
        if isinstance(symbol, str):
            self.symbol =symbol
        else:
            raise JinxSymbolError("Please input a symbol.")
        self.symbol = symbol

    def get_company(self):
        """Gets company data about the stock.

        Reference: https://iexcloud.io/docs/api/#company

        Data Weighting: ``1`` per symbol

        Returns
        -------
        dict
            Company data
        """
        path = "/stock/{}/company".format(self.symbol)
        params = {}
        return self._execute_iex_json_request(path=path, params=params)

    def get_cash_flow(self, period='quarter', last=1):
        """Pulls cash flow data. Available quarterly or annually.

        Reference: https://iexcloud.io/docs/api/#cash-flow

        Data Weighting: ``1000`` per symbol per period

        Parameters
        ----------
        period: str, default ``quarter``, optional
            Allows you to specify annual or quarterly cash flows. Defaults to
            quarterly. Values should be ``annual`` or ``quarter``.

        last: int, default ``1``, optional
            Specify the number of quarters or years to return.
            One quarter is returned by default. You can specify up to 12
            quarters with ``quarter``, or up to 4 years with ``annual``.

        Returns
        ------
        dict
            Stocks Cash Flow endpoint data
        """
        path = "/stock/{}/cash-flow".format(self.symbol)
        params = {'period':period, 'last':last}
        return self._execute_iex_json_request(path=path, params=params)

    def get_balance_sheet(self, period='quarter', last=1):
        """Pulls balance sheet data. Available quarterly or annually.

        Reference: https://iexcloud.io/docs/api/#balance-sheet

        Data Weighting: ``3000`` per symbol per period

        Parameters
        ----------
        period: str, default ``quarter``, optional
            Allows you to specify annual or quarterly cash flows. Defaults to
            quarterly. Values should be ``annual`` or ``quarter``.

        last: int, default ``1``, optional
            Specify the number of quarters or years to return.
            One quarter is returned by default. You can specify up to 12
            quarters with ``quarter``, or up to 4 years with ``annual``.

        Returns
        ------
        dict
            Stocks Balance Sheet endpoint data
        """
        path = "/stock/{}/balance-sheet".format(self.symbol)
        params = {'period':period, 'last':last}
        return self._execute_iex_json_request(path=path, params=params)

    def get_income_statement(self, period='quarter', last=1):
        """Pulls income statement data. Available quarterly or annually.

        Reference: https://iexcloud.io/docs/api/#income-statement

        Data Weighting: ``1000`` per symbol per period

        Parameters
        ----------
        period: str, default ``quarter``, optional
            Allows you to specify annual or quarterly cash flows. Defaults to
            quarterly. Values should be annual or quarter.

        last: int, default ``1``, optional
            Specify the number of quarters or years to return.
            One quarter is returned by default. You can specify up to 12
            quarters with ``quarter``, or up to 4 years with ``annual``.

        Returns
        ------
        dict
            Stocks Income Statement endpoint data
        """
        path = "/stock/{}/income".format(self.symbol)
        params = {'period':period, 'last':last}
        return self._execute_iex_json_request(path=path, params=params)

    def get_latest_financial_report_date(self):
        """Gets report date of latest financial report using data points.

        Reference: https://iexcloud.io/docs/api/#data-points

        Data Weighting: ``1``

        Returns
        ------
        dict
            Dictionary with one key: ``latestFinancialReportDate``
        """

        path = "/data-points/{}/LATEST-FINANCIAL-REPORT-DATE".format(
            self.symbol)
        params = {}

        text = self._execute_iex_text_request(path=path, params=params)
        stripped_text = text.replace('"',"")
        result_dict = {'latestFinancialReportDate':stripped_text}
        return result_dict
