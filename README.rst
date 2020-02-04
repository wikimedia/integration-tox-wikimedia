tox-wikimedia
=============

Automatically configure tox environments to use standard tools in a
hopefully unobtrusive way.

For example::

    [tox]
    envlist=py{34,35,36,37}-{flake8,pytest}
    skip_missing_interpreters = True
    requires = tox-wikimedia

    [wikimedia]

The following tools are supported for now:

flake8
------
flake8_: "the modular source code checker: pep8, pyflakes and co"

Command executed: ``flake8``

Dependencies installed: ``flake8``

pytest
------
pytest_: "pytest: simple powerful testing with Python"

Command executed: ``pytest``

Dependencies installed: ``pytest``, ``requirements.txt`` (if exists),
``test-requirements.txt`` (if exists)

.. _flake8: https://pypi.org/project/flake8/
.. _pytest: https://pytest.org/en/latest/
