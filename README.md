# pypi-simple-cli
A wrapper for [pypi-simple](https://github.com/jwodder/pypi-simple/tree/master)


|         |                                                                                                                                                                                                                                                                                                                                                                     |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CI/CD   | [![CI - Test](https://github.com/asurinsaka/pypi-simple-cli/actions/workflows/pytest.yaml/badge.svg)](https://github.com/asurinsaka/pypi-simple-cli/actions/workflows/pytest.yaml)                                                                                                                                                                                  |
| Package | [![PyPI - Version](https://img.shields.io/pypi/v/pypi-simple-cli?logo=pypi&label=PyPI&logoColor=gold)](https://pypi.org/project/pypi-simple-cli/) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pypi-simple-cli.svg?logo=python&label=Python&logoColor=gold)](https://pypi.org/project/pypi-simple-cli/)                                         |
| Meta    | [![code style - black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![License - Apache](https://img.shields.io/github/license/asurinsaka/pypi-simple-cli)](https://spdx.org/licenses/)|


## Example Usage:

```shell
> pypi-simple-cli list pypi-simple-cli
0.1.1

> pypi-simple-cli latest pypi-simple-cli
0.1.1

> pypi-simple-cli list requests 2.9
2.9.0
2.9.1
2.9.2

> pypi-simple-cli --endpoint=https://nexus.osdc.io/service/rest/repository/browse/pypi-all/ --release-stage=final list gdcdatamodel2
2.6.8
3.0.0

```
