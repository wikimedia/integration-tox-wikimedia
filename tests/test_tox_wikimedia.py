"""
Copyright (C) 2019-2020 Kunal Mehta <legoktm@debian.org>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""


def test_run(initproj, cmd):
    initproj(
        "pkg123-0.7",
        filedefs={
            "tox.ini": """
                [tox]
                envlist = py-{flake8,pytest}
                requires = tox-wikimedia
                [wikimedia]
            """
        },
    )
    result = cmd()
    output = result.output()
    assert "py-flake8 installdeps: flake8" in output
    assert "py-flake8 run-test: commands[0] | flake8" in output
    assert "py-pytest installdeps: pytest" in output
    assert "py-pytest run-test: commands[0] | pytest" in output


def test_parameterization(initproj, cmd):
    initproj(
        "pkg123-0.7",
        filedefs={
            "tox.ini": """
                [tox]
                envlist = py3-{mypy}
                requires = tox-wikimedia

                [wikimedia]
                mypy_package = foobar
            """
        },
    )
    result = cmd()
    output = result.output()
    print(output)
    assert "py3-mypy installdeps: mypy" in output
    assert "py3-mypy run-test: commands[0] | mypy foobar\n" in output


def test_disabled_run(initproj, cmd):
    initproj(
        "pkg123-0.7",
        filedefs={
            # Note that there's no [wikimedia] block below, so it should be
            # disabled even though it's required
            "tox.ini": """
                [tox]
                envlist = py-{flake8,pytest}
                requires = tox-wikimedia
            """
        },
    )
    result = cmd()
    output = result.output()
    assert "py-flake8 installdeps: flake8" not in output
    assert "py-flake8 run-test: commands[0] | flake8" not in output
    assert "py-pytest installdeps: pytest" not in output
    assert "py-pytest run-test: commands[0] | pytest" not in output
