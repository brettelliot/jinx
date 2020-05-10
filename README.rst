====
jinx
====

``jinx`` the Json INvestor eXchange package is a python SDK for getting financial data from IEX (the Investor Exchange) as JSON objects using the IEX Cloud API.

For more documentation, please see http://jinx.readthedocs.io.

Description
-----------

This package was heavily based off of `iexfinance`_ however that project uses pandas which doesn't work great when using docker and alpine. This package primarily exists to only return JSON.

.. _`iexfinance`: https://github.com/addisonlynch/iexfinance

Install
-------

From PyPI with pip (latest stable release):

.. code:: bash

    $ pip3 install jinx

From development repository (dev version):

.. code:: bash

     $ git clone https://github.com/brettelliot/jinx.git
     $ cd jinx
     $ python3 setup.py install

Authentication
--------------

An IEX Cloud account is required to acecss the IEX Cloud API. Various `plans <https://iexcloud.io/pricing/>`__
are availalbe, free, paid, and pay-as-you-go.

Your IEX Cloud (secret) authentication token can be passed to any function or at the instantiation of a ``Stock`` object.
The easiest way to store a token is in the ``IEX_TOKEN`` environment variable.

The desired IEX API version can be specified using the ``IEX_API_VERSION``
environment variable. The following versions are currently supported:

* ``v1`` - **default** (now same as ``iexcloud-v1``)
* ``iexcloud-beta``
* ``iexcloud-v1``
* ``iexcloud-sandbox`` - for use with the `sandbox environment`_ (test token
  must be used)

.. _`sandbox environment`: https://iexcloud.io/docs/api/#sandbox

Usage
-----

The ``Stock`` provides access to most endpoints, and can be instantiated with a symbol:

.. code-block:: python

        >>> from jinx.stock import Stock
        >>> import json
        >>> aapl = Stock('aapl')
        >>> aapl_bs = aapl.get_balance_sheet()
        >>> print (json.dumps(aapl_bs, sort_keys=True, indent=4))
        {
            "balancesheet": [
                {
                    "accountsPayable": 33018121739,
                    "capitalSurplus": null,
                    "commonStock": 4496599335,
                    "currency": "USD",
                    "currentAssets": 144612403174,
                    "currentCash": 30172961915,
                    "currentLongTermDebt": 10881096169,
                    "fiscalDate": "2020-03-22",
                    "goodwill": null,
                    "intangibleAssets": null,
                    "inventory": 3498769850,
                    "longTermDebt": 101705344870,
                    "longTermInvestments": 102909761019,
                    "minorityInterest": 0,
                    "netTangibleAssets": 78477657414,
                    "otherAssets": 33597449752,
                    "otherCurrentAssets": 14914938794,
                    "otherCurrentLiabilities": 42539380185,
                    "otherLiabilities": 21528724378,
                    "propertyPlantEquipment": 44907661177,
                    "receivables": 15986486509,
                    "reportDate": "2020-03-20",
                    "retainedEarnings": 33344074958,
                    "shareholderEquity": 80276696449,
                    "shortTermInvestments": 67226412874,
                    "totalAssets": 325814813094,
                    "totalCurrentLiabilities": 96306268790,
                    "totalLiabilities": 245573706847,
                    "treasuryStock": null
                }
            ],
            "symbol": "AAPL"
        }

You can get quarterly or annual data, and specify the number of quarters or years to return:

.. code-block:: python

        >>> aapl_cf = aapl.get_cash_flow(period='annual', last=2)
        >>> print(json.dumps(aapl_cf, sort_keys=True, indent=4))
        {
            "cashflow": [
                {
                    "capitalExpenditures": -10548387365,
                    "cashChange": 25028153575,
                    "cashFlow": 71074668596,
                    "cashFlowFinancing": -94932114603,
                    "changesInInventories": -291703549,
                    "changesInReceivables": 265402510,
                    "currency": "USD",
                    "depreciation": 12783029260,
                    "dividendsPaid": -14346206432,
                    "exchangeRateEffect": null,
                    "fiscalDate": "2019-09-27",
                    "investingActivityOther": -1109270269,
                    "investments": 58502395335,
                    "netBorrowings": -7868025705,
                    "netIncome": 57051020492,
                    "otherFinancingCashFlows": -3031452489,
                    "reportDate": "2019-09-19",
                    "totalInvestingCashFlows": 47952023359
                },
                {
                    "capitalExpenditures": -13632715598,
                    "cashChange": 5844075612,
                    "cashFlow": 80737644970,
                    "cashFlowFinancing": -89912917113,
                    "changesInInventories": 830556162,
                    "changesInReceivables": -5367160638,
                    "currency": "USD",
                    "depreciation": 11177076598,
                    "dividendsPaid": -14268054186,
                    "exchangeRateEffect": null,
                    "fiscalDate": "2018-09-24",
                    "investingActivityOther": -775705637,
                    "investments": 32259623849,
                    "netBorrowings": 436890215,
                    "netIncome": 62431044712,
                    "otherFinancingCashFlows": -2573213034,
                    "reportDate": "2018-09-27",
                    "totalInvestingCashFlows": 16703213665
                }
            ],
            "symbol": "AAPL"
        }
