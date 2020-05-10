============
Contributing
============

Developement notes
------------------

Installation for development::

    python setup.py develop

Testing::

    python setup.py test

Building the docs and packages
-----------------
First make sure sphinx is installed::

    pip install sphinx wheel twine

Then run::

    python setup.py docs

Test the docs with::

    python setup.py doctest

A simple rebase git workflow
----------------------------
Feature development workflow consists of these steps:

.. code-block:: bash

    # 1. Pull to update your local master
    git checkout master
    git pull origin master

    # 2. Check out a feature branch
    git checkout -b be-feature

    # 2. Or switch to it if it already exists
    git checkout be-feature

    # 3a. Do work in your feature branch, committing early and often. If you want to commit all your changes at once:
    git add .

    # 3b. If you want to commit patches one at a time:
    git add -p

    # 3c. Now add a message
    git commit -m "my changes"

    # 3d. Push your changes. First push?
    git push --set-upstream origin be-feature

    # 3e. Repeat pushes:
    git push

    # 4. Rebase frequently to incorporate upstream changes
    # Get stuff from origin master, then apply my changes on top with rebase
    git fetch origin master
    git rebase origin/master

    # 5. Interactive rebase (squash) your commits
    git rebase -i origin/master

    # I think maybe i had to do this?
    git push

    # 6. Merge your changes with master
    git checkout master
    git merge be-feature

    # 7. Push your changes to the remote
    git push origin master

    # 8a. optional: tag important things, such as releases
    git tag v1.0.0

    # 8b. push single tag
    git push origin v1.0.0

    # 8c. Push all tags
    git push origin --tags

    # 9a. Go back to your feature branch and do more work
    git checkout be-feature

    # 9b. Replay your changes on top of your feature branch
    git pull

Building a release
------------------
.. code-block:: bash

    # First add a tag
    git tag v1.0.3
    git push origin v1.0.3

    # Check the version
    python setup.py --version

    # remove any existinig distributon:
    rm -rf dist/

    # Build wheel distribution, just run:
    python setup.py bdist_wheel

    # Upload to test.pypi.org:
    twine upload --repository-url https://test.pypi.org/legacy/ dist/*

    # Test it. First, make a new test directory somewhere outside this project
    # Then make a virtual env for it
    # Then finally install from test.pypi.org:
    python3 -m pip install --no-cache-dir --extra-index-url https://test.pypi.org/simple/ jinx

    # Run python from the command line and import the package:
    python
    >>> from jinx.stock import Stock
    
    # After you've tested it, remove the test dir and begin the upload to pypi:
    twine upload dist/*

    # Now test the real deal... Make another test directory, make a virtual env,
    # and install from pip
    pip install --no-cache-dir jinx

    # Then run python import the package, and test it.
    python
    >>> from jinx.stock import Stock

PyScaffold
----------
This project has been set up using PyScaffold 3.2.3. For details and usage
information on PyScaffold see https://pyscaffold.org/.


