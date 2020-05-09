====
jinx
====

A python SDK for getting JSON objects from the IEX Cloud API.


Description
-----------

This package was heavily based off of `iexfinance`_ however that project uses pandas which doesn't work great when using docker and alpine. This package primarily exists to only return JSON.

.. _`iexfinance`: https://github.com/addisonlynch/iexfinance

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

.. _`sandbox environment`: https://iexcloud.io/docs/api/#sandboxa


Developement notes
-----------------

**Installation for development**
```bash
python setup.py develop
```

**Testing**
```bash
python setup.py test
```

**Building the docs** 
First make sure sphinx is installed: 
```bash
pip install sphinx
```
Then run: 
```bash
python setup.py docs
```
Test the docs with:
```bash
python setup.py doctest
```


In order to build a source, binary or wheel distribution, just run 
`python setup.py sdist`, `python setup.py bdist` or `python setup.py bdist_wheel` (recommended).

Run `python setup.py --version` to retrieve the current PEP440-compliant version. This version will be used when building a package and is also accessible through my_project.__version__. If you want to upload to PyPI you have to tag the current commit before uploading since PyPI does not allow local versions, e.g. 0.0.post0.dev5+gc5da6ad, for practical reasons.

This project has been set up using PyScaffold 3.2.3. For details and usage
information on PyScaffold see https://pyscaffold.org/.
