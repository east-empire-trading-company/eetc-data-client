# EETC Data Client
Python client for consuming the [EETC Data Hub REST API](https://eetc.readme.io/reference/price-data).
Used for retrieving data managed by [EETC Data Hub](https://github.com/east-empire-trading-company/eetc_data_hub).

## Examples
```python
"""
Getting historical daily price data for AAPL.
"""

from eetc_data_client.client import EETCDataClient

client = EETCDataClient(api_key="getYourApiKeyFromUsOnRequest")

aapl_price_data_df = client.get_price_data("AAPL")
print(aapl_price_data_df.head())

china_exports_data = client.get_macroeconomic_data(
    "Exports in USD - China", frequency="Monthly",
)
print(china_exports_data.head())
```

```python
"""
Getting historical fundamentals data for AAPL.
"""

from eetc_data_client.client import EETCDataClient

client = EETCDataClient(api_key="getYourApiKeyFromUsOnRequest")

aapl_fundamentals_data_df = client.get_fundamentals_data("AAPL", frequency="Quarterly")
print(aapl_fundamentals_data_df.head())
```

```python
"""
Getting historical macroeconomic data for Chinese exports.
"""

from eetc_data_client.client import EETCDataClient

client = EETCDataClient(api_key="getYourApiKeyFromUsOnRequest")

china_exports_data_df = client.get_macroeconomic_data("Exports in USD - China")
print(china_exports_data_df.head())
```

## Available macroeconomic data
- Imports in USD - China
- NMI - Inventory Sentiment
- PMI - Backlog of Orders
- Imports in USD - Brazil
- NMI - Business Activity
- PMI - Inventories
- PMI - Supplier Deliveries
- PMI - Production
- Exports in USD - United Kingdom
- Imports in USD - United Kingdom
- NMI - New Orders
- NMI - Employment
- Exports in USD - France
- Exports in USD - Italy
- Exports in USD - India
- Inflation YoY - US
- NMI - Backlog of Orders
- NMI - Inventories
- Exports in USD - Germany
- PMI
- Imports in USD - Canada
- PMI - New Export Orders
- Inflation YoY - EU
- Inflation YoY - Germany
- CPI - EU
- PMI - Imports
- NMI - New Export Orders
- NMI - Prices
- PMI - New Orders
- Imports in USD - Japan
- Exports in USD - China
- US 5-Year 5Year Forward Inflation Expectation Rate
- PMI - Customer Inventories
- US Consumer Sentiment Index
- CPI - Germany
- Exports in USD - United States
- US Total Public Debt as Percent of Gross Domestic Product
- NMI - Supplier Deliveries
- US Real GDP
- Imports in USD - United Arab Emirates
- Imports in USD - France
- PMI - Prices
- Imports in USD - United States
- Exports in USD - United Arab Emirates
- Imports in USD - Germany
- Imports in USD - India
- Imports in USD - Italy
- CPI - US
- Exports in USD - Canada
- Exports in USD - Japan
- Exports in USD - Brazil
- PMI - Employment
- NMI
- FED - Total Securities Purchased in Repurchase Agreements
- FED - Total Securities Sold in Reverse Repurchase Agreements
- US - 10-Year Treasury Constant Maturity minus 2-Year Treasury Constant Maturity
- US - 10-Year Breakeven Inflation Rate
- US - 5-Year Breakeven Inflation Rate
- FED - 8-District Flexible Rate on Seasonal Credit
- FED - Overnight Bank Funding Rate

# Development

## System requirements
To run the project locally and work on it, you need the following:
- Python 3.8+

## Project setup
```commandline
sudo apt-get install build-essential
make update_and_install_python_requirements
```

## Adding a new Python package
1. Add the package name to `requirements.in`
2. Run:
```commandline
make update_and_install_python_requirements
```

## Publishing new package versions to PyPi
1. Update `[build_system]` section in `pyproject.toml` in case new dependencies are added or existing dependency versions were updated.
2. Update `version` field in `[project]` section in `pyproject.toml` whenever there is a new change to the project.
3. Build the project using command:
```commandline
python -m build
```
4. Publish package on PyPi Test, run command:
```commandline
python -m twine upload --repository testpypi dist/*
```
4. If everything is ok on PyPi Test, publish on "real" PyPi using the command:
```commandline
python -m twine upload --repository pypi dist/*
```
