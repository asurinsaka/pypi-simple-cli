import os
import pathlib

import requests_mock
from click.testing import CliRunner

from pypi_simple_cli import cli

PYPI_SIMPLE_ENDPOINT: str = "https://pypi.org/simple/"
DATA_DIR = pathlib.Path(os.path.dirname(os.path.realpath(__file__))) / "data"


@requests_mock.Mocker(kw="mock")
def test_list_indexd(**kwargs):
    with (DATA_DIR / "fake_page.html").open() as f:
        kwargs["mock"].get(f"{PYPI_SIMPLE_ENDPOINT}indexd/", text=f.read())
    runner = CliRunner()
    result = runner.invoke(
        cli.main,
        [
            "list",
            "indexd",
        ],
    )
    assert result.stdout == (
        "1.0.0\n1.2.3a4\n1.2.3b4\n1.2.3rc4\n1.2.3rc5\n2.13.3.dev2\n2.14.0\n"
        "3.0.2.dev6+feat.dev.2298.use.different.post.fix.for.version\n"
    )


@requests_mock.Mocker(kw="mock")
def test_latest_indexd(**kwargs):
    with (DATA_DIR / "fake_page.html").open() as f:
        kwargs["mock"].get(f"{PYPI_SIMPLE_ENDPOINT}indexd/", text=f.read())
    runner = CliRunner()
    result = runner.invoke(
        cli.main,
        [
            "latest",
            "indexd",
        ],
    )
    assert (
        result.stdout == "3.0.2.dev6+feat.dev.2298.use.different.post.fix.for.version"
    )
