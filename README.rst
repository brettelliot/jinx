====
jinx
====

A python package for getting JSON objects from the IEX Cloud API.


Description
-----------

This package was heavily based off of `iexfinance`_ however that project uses pandas which doesn't work great when using docker and alpine. This package primarily exists to only return JSON.

.. _`iexfinance`: https://github.com/addisonlynch/iexfinance

Install
-------

From PyPI with pip (latest stable release):

``$ pip3 install jinx``

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

The ``Stock`` provides access to most endpoints, and can be instantiated with a symbols:

.. code-block:: python

    from jinx.stock import Stock

    aapl = Stock("AAPL")
    json_response = aapl.get_balance_sheet()

.. code-block:: json

        {'balancesheet': [{'accountsPayable': 33112195828,
                   'capitalSurplus': None,
                   'commonStock': 4346699683,
                   'currency': 'USD',
                   'currentAssets': 147028486806,
                   'currentCash': 30036272090,
                   'currentLongTermDebt': 10665375192,
                   'fiscalDate': '2020-03-13',
                   'goodwill': None,
                   'intangibleAssets': None,
                   'inventory': 3434799069,
                   'longTermDebt': 99355148492,
                   'longTermInvestments': 102046592090,
                   'minorityInterest': 0,
                   'netTangibleAssets': 80858422273,
                   'otherAssets': 33551375884,
                   'otherCurrentAssets': 15195434566,
                   'otherCurrentLiabilities': 42099581013,
                   'otherLiabilities': 21024755946,
                   'propertyPlantEquipment': 45201912330,
                   'receivables': 16017799523,
                   'reportDate': '2020-03-21',
                   'retainedEarnings': 34747214319,
                   'shareholderEquity': 78782314016,
                   'shortTermInvestments': 68349274002,
                   'totalAssets': 334142170974,
                   'totalCurrentLiabilities': 97157853580,
                   'totalLiabilities': 244626756872,
                   'treasuryStock': None}],
        'symbol': 'AAPL'}

.. code-block:: python

        json_response = aapl.get_cash_flow(period='annual', last=2)

.. code-block:: json

        {'cashflow': [{'capitalExpenditures': -10770004070,
               'cashChange': 24863353536,
               'cashFlow': 72204258940,
               'cashFlowFinancing': -92351448945,
               'changesInInventories': -300397389,
               'changesInReceivables': 264718035,
               'currency': 'USD',
               'depreciation': 13116848608,
               'dividendsPaid': -14503573256,
               'exchangeRateEffect': None,
               'fiscalDate': '2019-09-25',
               'investingActivityOther': -1109360682,
               'investments': 59220343455,
               'netBorrowings': -7894824202,
               'netIncome': 56633880619,
               'otherFinancingCashFlows': -3061111157,
               'reportDate': '2019-09-20',
               'totalInvestingCashFlows': 47753822021},
              {'capitalExpenditures': -13939233622,
               'cashChange': 5790071745,
               'cashFlow': 80050783491,
               'cashFlowFinancing': -91406242732,
               'changesInInventories': 829147940,
               'changesInReceivables': -5555305538,
               'currency': 'USD',
               'depreciation': 11135992882,
               'dividendsPaid': -14260530107,
               'exchangeRateEffect': None,
               'fiscalDate': '2018-09-16',
               'investingActivityOther': -764234805,
               'investments': 32104361274,
               'netBorrowings': 435808335,
               'netIncome': 60452479349,
               'otherFinancingCashFlows': -2566982008,
               'reportDate': '2018-09-28',
               'totalInvestingCashFlows': 16068508327}],
        'symbol': 'AAPL'}
