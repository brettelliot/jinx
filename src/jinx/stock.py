import logging
import requests
from jinx.base import _JinxBase
from jinx.exceptions import JinxSymbolError

logger = logging.getLogger(__name__)

class Stock(_JinxBase):
    """
    Base class for obtaining data from the Stock endpoints of IEX.
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
            raise JinxSymbolError("Please input a symbol or list of symbols")
        self.symbol = symbol

    def get_company(self):
        path = "/stock/{}/company".format(self.symbol)
        params = {}
        return self._execute_iex_json_request(path=path, params=params)

    def get_cash_flow(self, period='quarterly', last=1):
        """Cash Flow
        Pulls cash flow data. Available quarterly or annually.
        Reference: https://iexcloud.io/docs/api/#cash-flow
        Data Weighting: ``1000`` per symbol per period

        Parameters
        ----------
        period: str, default 'quarterly', optional
            Allows you to specify annual or quarterly cash flows. Defaults to
            quarterly. Values should be annual or quarter.

        last: int, default 1, optional
            Specify the number of quarters or years to return.
            One quarter is returned by default. You can specify up to 12
            quarters with quarter, or up to 4 years with annual.

        Returns
        ------
        dict
            Stocks Cash Flow endpoint data
        """
        path = "/stock/{}/cash-flow".format(self.symbol)
        params = {'period':period, 'last':last}
        return self._execute_iex_json_request(path=path, params=params)

    def get_balance_sheet(self, period='quarterly', last=1):
        """Balance Sheet
        Pulls balance sheet data. Available quarterly or annually.
        Reference: https://iexcloud.io/docs/api/#balance-sheet
        Data Weighting: ``3000`` per symbol per period

        Parameters
        ----------
        period: str, default 'quarterly', optional
            Allows you to specify annual or quarterly cash flows. Defaults to
            quarterly. Values should be annual or quarter.

        last: int, default 1, optional
            Specify the number of quarters or years to return.
            One quarter is returned by default. You can specify up to 12
            quarters with quarter, or up to 4 years with annual.

        Returns
        ------
        dict
            Stocks Balance Sheet endpoint data
        """
        path = "/stock/{}/balance-sheet".format(self.symbol)
        params = {'period':period, 'last':last}
        return self._execute_iex_json_request(path=path, params=params)

    def get_income_statement(self, period='quarterly', last=1):
        """Income Statement
        Pulls income statement data. Available quarterly or annually.
        Reference: https://iexcloud.io/docs/api/#income-statement
        Data Weighting: ``1000`` per symbol per period

        Parameters
        ----------
        period: str, default 'quarterly', optional
            Allows you to specify annual or quarterly cash flows. Defaults to
            quarterly. Values should be annual or quarter.

        last: int, default 1, optional
            Specify the number of quarters or years to return.
            One quarter is returned by default. You can specify up to 12
            quarters with quarter, or up to 4 years with annual.

        Returns
        ------
        dict
            Stocks Income Statement endpoint data
        """
        path = "/stock/{}/income".format(self.symbol)
        params = {'period':period, 'last':last}
        return self._execute_iex_json_request(path=path, params=params)

    def get_latest_financial_report_date(self):
        path = "/data-points/{}/LATEST-FINANCIAL-REPORT-DATE".format(
            self.symbol)
        params = {}

        text = self._execute_iex_text_request(path=path, params=params)
        result_dict = {'latestFinancialReportDate':text}
        return result_dict
