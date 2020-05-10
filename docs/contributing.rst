============
Contributing
============

Developement notes
------------------

Installation for development::

    python setup.py develop

Testing::

    python setup.py test

Building the docs
-----------------
First make sure sphinx is installed::

    pip install sphinx

Then run::

    python setup.py docs

Test the docs with::

    python setup.py doctest

Building a release
------------------
In order to build a source, binary or wheel distribution, just run
`python setup.py sdist`, `python setup.py bdist` or `python setup.py bdist_wheel` (recommended).

Run `python setup.py --version` to retrieve the current PEP440-compliant version. This version will be used when building a package and is also accessible through my_project.__version__. If you want to upload to PyPI you have to tag the current commit before uploading since PyPI does not allow local versions, e.g. 0.0.post0.dev5+gc5da6ad, for practical reasons.

This project has been set up using PyScaffold 3.2.3. For details and usage
information on PyScaffold see https://pyscaffold.org/.
