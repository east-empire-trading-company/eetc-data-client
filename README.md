# EETC Data Client
Python client for consuming the [EETC Data Hub REST API](https://eetc.readme.io/reference/price-data).
Used for retrieving data managed by [EETC Data Hub](https://github.com/east-empire-trading-company/eetc_data_hub).

### Usage examples
```python
"""
Getting historical daily price data for AAPL.
"""

from eetc_data_client.client import EETCDataClient

client = EETCDataClient(api_key="getYourApiKeyFromUsOnRequest")

aapl_price_data_df = client.get_price_data("AAPL")
print(aapl_price_data_df.head())
```

```python
"""
Getting fundamentals for AAPL.
"""

from eetc_data_client.client import EETCDataClient

client = EETCDataClient(api_key="getYourApiKeyFromUsOnRequest")

aapl_fundamentals_data_df = client.get_fundamentals_data("AAPL", frequency="Quarterly")
print(aapl_fundamentals_data_df.head())
```

```python
"""
Getting (macroeconomic) indicator data for Chinese exports.
"""

from eetc_data_client.client import EETCDataClient

client = EETCDataClient(api_key="getYourApiKeyFromUsOnRequest")

china_exports_data_df = client.get_macroeconomic_data("Exports in USD - China")
print(china_exports_data_df.head())
```

### Available (macroeconomic) indicators
To get the available (macroeconomic) indicators use the `get_indicators()` method.
"""
Getting historical macroeconomic data for Chinese exports.
"""

```python
from eetc_data_client.client import EETCDataClient

client = EETCDataClient(api_key="getYourApiKeyFromUsOnRequest")

indicators = client.get_indicators()
print(indicators)
```

## Development

### System requirements
To run the project locally and work on it, you need the following:
- Python 3.8+

### Project setup
```commandline
sudo apt-get install build-essential
make update_and_install_python_requirements
```

### Adding a new Python package
1. Add the package name to `requirements.in`
2. Run:
```commandline
make update_and_install_python_requirements
```

### Publishing new package versions to PyPi
1. Update `[build_system]` section in `pyproject.toml` in case new dependencies are added or existing dependency versions were updated.
2. Update `version` field in `[project]` section in `pyproject.toml` whenever there is a new change to the project.
3. Publish package on PyPi Test, run command:
```commandline
make publish_package_on_pypi_test
```
4. If everything is ok on PyPi Test, publish on "real" PyPi using the command:
```commandline
make publish_package_on_pypi
```
