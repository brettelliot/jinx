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
``python setup.py sdist``, ``python setup.py bdist`` or ``python setup.py bdist_wheel`` (recommended).

Run ``python setup.py --version`` to retrieve the current PEP440-compliant version. This version will be used when building a package and is also accessible through my_project.__version__. If you want to upload to PyPI you have to tag the current commit before uploading since PyPI does not allow local versions, e.g. 0.0.post0.dev5+gc5da6ad, for practical reasons.

This project has been set up using PyScaffold 3.2.3. For details and usage
information on PyScaffold see https://pyscaffold.org/.


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
    git tag 1.0.0

    # 8b. push single tag
    git push origin 1.0.0

    # 8c. Push all tags
    git push origin --tags

    # 9a. Go back to your feature branch and do more work
    git checkout be-feature

    # 9b. Replay your changes on top of your feature branch
    git pull
