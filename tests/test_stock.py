import pytest
from jinx.stock import Stock

class TestStock(object):

    def test_get_latest_financial_report_date(self):
        stock = Stock('AAPL')
        json_response = stock.get_latest_financial_report_date()
        assert 'latestFinancialReportDate' in json_response

    def test_get_company(self):
        stock = Stock('AAPL')
        json_response = stock.get_company()
        assert 'symbol' in json_response
        assert 'companyName' in json_response
        assert 'industry' in json_response
        assert 'description' in json_response
        assert 'sector' in json_response
        assert 'exchange' in json_response

    def test_get_cash_flow(self):
        stock = Stock('AAPL')
        json_response = stock.get_cash_flow()
        assert 'cashflow' in json_response
        data = json_response['cashflow'][0]
        assert 'reportDate' in data
        assert 'fiscalDate' in data
        assert 'netIncome' in data

    def test_get_cash_flow_last_5_years(self):
        stock = Stock('AAPL')
        json_response = stock.get_cash_flow(period='annual', last=5)
        assert 'cashflow' in json_response
        length = len(json_response['cashflow'])
        assert length is 5
        for x in json_response['cashflow']:
            assert 'reportDate' in x
            assert 'fiscalDate' in x
            assert 'netIncome' in x

    def test_get_balance_sheet(self):
        stock = Stock('AAPL')
        json_response = stock.get_balance_sheet()
        assert 'balancesheet' in json_response
        data = json_response['balancesheet'][0]
        assert 'currentCash' in data
        assert 'shortTermInvestments' in data
        assert 'totalAssets' in data

    def test_get_balance_sheet_last_8_quarters(self):
        stock = Stock('AAPL')
        json_response = stock.get_balance_sheet(period='quarterly', last=8)
        assert 'balancesheet' in json_response
        length = len(json_response['balancesheet'])
        assert length is 8
        for x in json_response['balancesheet']:
            assert 'currentCash' in x
            assert 'shortTermInvestments' in x
            assert 'totalAssets' in x

    def test_get_income_statement(self):
        stock = Stock('AAPL')
        json_response = stock.get_income_statement()
        assert 'income' in json_response
        data = json_response['income'][0]
        assert 'ebit' in data
        assert 'totalRevenue' in data
        assert 'operatingIncome' in data

    def test_get_balance_sheet_last_8_quarters(self):
        stock = Stock('AAPL')
        json_response = stock.get_income_statement(period='quarterly', last=8)
        assert 'income' in json_response
        length = len(json_response['income'])
        assert length is 8
        for x in json_response['income']:
            assert 'ebit' in x
            assert 'totalRevenue' in x
            assert 'operatingIncome' in x
