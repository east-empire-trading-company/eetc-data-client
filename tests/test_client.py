import unittest
from unittest import mock
from unittest.mock import MagicMock

import pandas as pd
from pandas._testing import assert_frame_equal

from src.eetc_data_client.client import EETCDataClient


class TestEETCDataClient(unittest.TestCase):
    def assertDataFrameEqual(self, a, b, msg):
        try:
            assert_frame_equal(a, b)
        except AssertionError as e:
            raise self.failureException(msg) from e

    def setUp(self):
        # set up a custom method for checking pandas DataFrame equality
        self.addTypeEqualityFunc(pd.DataFrame, self.assertDataFrameEqual)
        self.eetc_data_client = EETCDataClient("test_api_key")

    def test_get_price_data(self):
        # given
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json = MagicMock(
            return_value=[
                {
                    "date": "2012-04-26T00:00:00Z",
                    "symbol": "AAPL",
                    "source": "YahooFinance",
                    "open": 21.94,
                    "high": 21.95,
                    "low": 21.5,
                    "close": 21.7,
                    "volume": 536068400.0,
                    "inserted_at": None,
                    "name": "Apple Inc.",
                },
            ],
        )
        symbol = "AAPL"
        expected = pd.json_normalize(
            [
                {
                    "date": "2012-04-26T00:00:00Z",
                    "symbol": "AAPL",
                    "source": "YahooFinance",
                    "open": 21.94,
                    "high": 21.95,
                    "low": 21.5,
                    "close": 21.7,
                    "volume": 536068400.0,
                    "inserted_at": None,
                    "name": "Apple Inc.",
                },
            ],
        )

        # when
        with mock.patch(
            "eetc_data_client.client.EETCDataClient._send_http_request",
            return_value=mock_response,
        ):
            data = self.eetc_data_client.get_price_data(symbol)

        # then
        self.assertEqual(data, expected)

    def test_get_price_data_as_json(self):
        # given
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json = MagicMock(
            return_value=[
                {
                    "date": "2012-04-26T00:00:00Z",
                    "symbol": "AAPL",
                    "source": "YahooFinance",
                    "open": 21.94,
                    "high": 21.95,
                    "low": 21.5,
                    "close": 21.7,
                    "volume": 536068400.0,
                    "inserted_at": None,
                    "name": "Apple Inc.",
                },
            ],
        )
        symbol = "AAPL"
        expected = [
            {
                "date": "2012-04-26T00:00:00Z",
                "symbol": "AAPL",
                "source": "YahooFinance",
                "open": 21.94,
                "high": 21.95,
                "low": 21.5,
                "close": 21.7,
                "volume": 536068400.0,
                "inserted_at": None,
                "name": "Apple Inc.",
            },
        ]

        # when
        with mock.patch(
            "eetc_data_client.client.EETCDataClient._send_http_request",
            return_value=mock_response,
        ):
            data = self.eetc_data_client.get_price_data(symbol, as_json=True)

        # then
        self.assertEqual(expected, data)

    def test_get_fundamentals_data(self):
        # given
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json = MagicMock(
            return_value=[
                {
                    "symbol": "AAPL",
                    "year": 2021,
                    "quarter": None,
                    "name": "Apple",
                    "inserted_at": None,
                    "frequency": "Yearly",
                    "source": "MarketWatch",
                    "revenue": 365820000000.0,
                    "cogs": 212980000000.0,
                    "cogs_excluding_deprecation_and_amortization": 201700000000.0,
                    "deprecation_and_amortization_expense": 11280000000.0,
                    "gross_profit": 152840000000.0,
                    "gross_profit_margin": 0.42,
                    "sga_expenses": 43890000000.0,
                    "research_and_development_expenses": 21910000000.0,
                    "unusual_expense": None,
                    "ebit": None,
                    "non_operating_income": 60000000.0,
                    "non_operating_interest_income": 2840000000.0,
                    "interest_expense": 2650000000.0,
                    "net_income_before_tax": 109210000000.0,
                    "income_tax": 14530000000.0,
                    "equity_in_affiliates": None,
                    "net_income_after_tax": None,
                    "other_after_tax_income": None,
                    "consolidated_net_income": 94680000000.0,
                    "minority_interest": None,
                    "net_income_before_extraordinaries": 94680000000.0,
                    "preferred_dividends": None,
                    "net_income_available_to_common": 94680000000.0,
                    "eps_basic": 5.67,
                    "basic_shares_outstanding": 16700000000.0,
                    "eps_diluted": 5.61,
                    "diluted_shares_outstanding": 16860000000.0,
                    "ebitda": 120230000000.0,
                    "net_income": 94680000000.0,
                    "deprecation_depletion_and_amortization": 11280000000.0,
                    "deprecation_depletion": 11280000000.0,
                    "amortization": None,
                    "deferred_taxes": None,
                    "investment_tax_credit": None,
                    "extraordinaries": None,
                    "changes_in_working_capital": -4910000000.0,
                    "accounts_receivables": -14030000000.0,
                    "accounts_payable": None,
                    "cash_from_operating_activities": 104040000000.0,
                    "capex": -11090000000.0,
                    "net_assets_from_acquisitions": -33000000.0,
                    "sale_of_fixed_assets_and_businesses": None,
                    "purchase_of_investments": -109690000000.0,
                    "sale_of_investments": 106870000000.0,
                    "cash_from_investing_activities": -14550000000.0,
                    "cash_dividends_paid": -14470000000.0,
                    "change_in_capital_stock": -84870000000.0,
                    "repurchase_of_common_and_preferred_stock": -85970000000.0,
                    "sale_of_common_and_preferred_stock": 1110000000.0,
                    "proceeds_from_stock_options": 1110000000.0,
                    "other_proceeds_from_sale_of_stock": None,
                    "change_in_debt": 12670000000.0,
                    "change_in_current_debt": 1020000000.0,
                    "change_in_long_term_debt": 11640000000.0,
                    "other_funds": -6690000000.0,
                    "cash_from_financing_activities": -93350000000.0,
                    "foreign_exchange_effect": None,
                    "miscellaneous_funds": None,
                    "net_change_in_cash": -3860000000.0,
                    "free_cash_flow": 92950000000.0,
                    "cash_and_short_term_investments": 62640000000.0,
                    "cash": 26910000000.0,
                    "short_term_investments": 35730000000.0,
                    "accounts_receivable": 51510000000.0,
                    "accounts_receivables_net": 26280000000.0,
                    "bad_debt_doubtful_accounts": None,
                    "other_receivable": 25230000000.0,
                    "accounts_receivable_turnover": 7.1,
                    "inventories": 6580000000.0,
                    "other_current_assets": 14110000000.0,
                    "total_current_assets": 134840000000.0,
                    "property_plant_equipment_net": 49530000000.0,
                    "property_plant_equipment_gross": 119810000000.0,
                    "buildings": 20040000000.0,
                    "land_and_improvements": None,
                    "computer_software_and_equipment": None,
                    "other_property_plant_equipment": 11020000000.0,
                    "accumulated_deprecation": 70280000000.0,
                    "total_investments_and_advances": 127880000000.0,
                    "long_term_note_receivables": None,
                    "intangible_assets": None,
                    "goodwill": None,
                    "other_intangibles": None,
                    "other_assets": 38760000000.0,
                    "total_assets": 351000000000.0,
                    "short_term_debt": 7450000000.0,
                    "current_portion_of_long_term_debt": 9690000000.0,
                    "accounts_payable_1": None,
                    "income_tax_payable": None,
                    "other_current_liabilities": 53580000000.0,
                    "total_current_liabilities": 125480000000.0,
                    "long_term_debt": 119380000000.0,
                    "provision_for_risks_and_charges": 24690000000.0,
                    "deferred_taxes_1": None,
                    "other_liabilities": 18360000000.0,
                    "deferred_income": None,
                    "total_liabilities": 287910000000.0,
                    "non_equity_reserves": None,
                    "preferred_stock": None,
                    "redeemable_preferred_stock": None,
                    "non_redeemable_preferred_stock": None,
                    "common_equity": 63090000000.0,
                    "retained_earnings": 5560000000.0,
                    "unrealized_gains_in_marketable_securities": None,
                    "treasury_stock": None,
                    "total_shareholders_equity": 63090000000.0,
                    "accumulated_minority_interest": None,
                    "total_equity": 63090000000.0,
                    "liabilities_and_shareholders_equity": 351000000000.0,
                }
            ],
        )
        symbol = "AAPL"
        frequency = "Yearly"
        year = 2021
        expected = pd.json_normalize(
            [
                {
                    "symbol": "AAPL",
                    "year": 2021,
                    "quarter": None,
                    "name": "Apple",
                    "inserted_at": None,
                    "frequency": "Yearly",
                    "source": "MarketWatch",
                    "revenue": 365820000000.0,
                    "cogs": 212980000000.0,
                    "cogs_excluding_deprecation_and_amortization": 201700000000.0,
                    "deprecation_and_amortization_expense": 11280000000.0,
                    "gross_profit": 152840000000.0,
                    "gross_profit_margin": 0.42,
                    "sga_expenses": 43890000000.0,
                    "research_and_development_expenses": 21910000000.0,
                    "unusual_expense": None,
                    "ebit": None,
                    "non_operating_income": 60000000.0,
                    "non_operating_interest_income": 2840000000.0,
                    "interest_expense": 2650000000.0,
                    "net_income_before_tax": 109210000000.0,
                    "income_tax": 14530000000.0,
                    "equity_in_affiliates": None,
                    "net_income_after_tax": None,
                    "other_after_tax_income": None,
                    "consolidated_net_income": 94680000000.0,
                    "minority_interest": None,
                    "net_income_before_extraordinaries": 94680000000.0,
                    "preferred_dividends": None,
                    "net_income_available_to_common": 94680000000.0,
                    "eps_basic": 5.67,
                    "basic_shares_outstanding": 16700000000.0,
                    "eps_diluted": 5.61,
                    "diluted_shares_outstanding": 16860000000.0,
                    "ebitda": 120230000000.0,
                    "net_income": 94680000000.0,
                    "deprecation_depletion_and_amortization": 11280000000.0,
                    "deprecation_depletion": 11280000000.0,
                    "amortization": None,
                    "deferred_taxes": None,
                    "investment_tax_credit": None,
                    "extraordinaries": None,
                    "changes_in_working_capital": -4910000000.0,
                    "accounts_receivables": -14030000000.0,
                    "accounts_payable": None,
                    "cash_from_operating_activities": 104040000000.0,
                    "capex": -11090000000.0,
                    "net_assets_from_acquisitions": -33000000.0,
                    "sale_of_fixed_assets_and_businesses": None,
                    "purchase_of_investments": -109690000000.0,
                    "sale_of_investments": 106870000000.0,
                    "cash_from_investing_activities": -14550000000.0,
                    "cash_dividends_paid": -14470000000.0,
                    "change_in_capital_stock": -84870000000.0,
                    "repurchase_of_common_and_preferred_stock": -85970000000.0,
                    "sale_of_common_and_preferred_stock": 1110000000.0,
                    "proceeds_from_stock_options": 1110000000.0,
                    "other_proceeds_from_sale_of_stock": None,
                    "change_in_debt": 12670000000.0,
                    "change_in_current_debt": 1020000000.0,
                    "change_in_long_term_debt": 11640000000.0,
                    "other_funds": -6690000000.0,
                    "cash_from_financing_activities": -93350000000.0,
                    "foreign_exchange_effect": None,
                    "miscellaneous_funds": None,
                    "net_change_in_cash": -3860000000.0,
                    "free_cash_flow": 92950000000.0,
                    "cash_and_short_term_investments": 62640000000.0,
                    "cash": 26910000000.0,
                    "short_term_investments": 35730000000.0,
                    "accounts_receivable": 51510000000.0,
                    "accounts_receivables_net": 26280000000.0,
                    "bad_debt_doubtful_accounts": None,
                    "other_receivable": 25230000000.0,
                    "accounts_receivable_turnover": 7.1,
                    "inventories": 6580000000.0,
                    "other_current_assets": 14110000000.0,
                    "total_current_assets": 134840000000.0,
                    "property_plant_equipment_net": 49530000000.0,
                    "property_plant_equipment_gross": 119810000000.0,
                    "buildings": 20040000000.0,
                    "land_and_improvements": None,
                    "computer_software_and_equipment": None,
                    "other_property_plant_equipment": 11020000000.0,
                    "accumulated_deprecation": 70280000000.0,
                    "total_investments_and_advances": 127880000000.0,
                    "long_term_note_receivables": None,
                    "intangible_assets": None,
                    "goodwill": None,
                    "other_intangibles": None,
                    "other_assets": 38760000000.0,
                    "total_assets": 351000000000.0,
                    "short_term_debt": 7450000000.0,
                    "current_portion_of_long_term_debt": 9690000000.0,
                    "accounts_payable_1": None,
                    "income_tax_payable": None,
                    "other_current_liabilities": 53580000000.0,
                    "total_current_liabilities": 125480000000.0,
                    "long_term_debt": 119380000000.0,
                    "provision_for_risks_and_charges": 24690000000.0,
                    "deferred_taxes_1": None,
                    "other_liabilities": 18360000000.0,
                    "deferred_income": None,
                    "total_liabilities": 287910000000.0,
                    "non_equity_reserves": None,
                    "preferred_stock": None,
                    "redeemable_preferred_stock": None,
                    "non_redeemable_preferred_stock": None,
                    "common_equity": 63090000000.0,
                    "retained_earnings": 5560000000.0,
                    "unrealized_gains_in_marketable_securities": None,
                    "treasury_stock": None,
                    "total_shareholders_equity": 63090000000.0,
                    "accumulated_minority_interest": None,
                    "total_equity": 63090000000.0,
                    "liabilities_and_shareholders_equity": 351000000000.0,
                }
            ],
        )

        # when
        with mock.patch(
            "eetc_data_client.client.EETCDataClient._send_http_request",
            return_value=mock_response,
        ):
            data = self.eetc_data_client.get_fundamentals_data(symbol,
                                                               frequency, year)

        # then
        self.assertEqual(data, expected)

    def test_get_macroeconomic_data(self):
        # given
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json = MagicMock(
            return_value=[
                {
                    "year": 2020,
                    "quarter": None,
                    "month": None,
                    "week": None,
                    "date": "2020-01-01T00:00:00Z",
                    "name": "US Real GDP",
                    "value": -3.4,
                    "inserted_at": None,
                    "frequency": "Yearly",
                }
            ]
        )
        name = "US Real GDP"
        frequency = "Yearly"
        from_date = "2020-01-01"
        to_date = "2020-12-30"
        expected = pd.json_normalize(
            [
                {
                    "year": 2020,
                    "quarter": None,
                    "month": None,
                    "week": None,
                    "date": "2020-01-01T00:00:00Z",
                    "name": "US Real GDP",
                    "value": -3.4,
                    "inserted_at": None,
                    "frequency": "Yearly",
                }
            ],
        )

        # when
        with mock.patch(
            "eetc_data_client.client.EETCDataClient._send_http_request",
            return_value=mock_response,
        ):
            data = self.eetc_data_client.get_macroeconomic_data(
                name, frequency, from_date, to_date
            )

        # then
        self.assertEqual(data, expected)

    def test_get_fundamentals_data_as_json(self):
        # given
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json = MagicMock(
            return_value=[
                {
                    "symbol": "AAPL",
                    "year": 2021,
                    "quarter": None,
                    "name": "Apple",
                    "inserted_at": None,
                    "frequency": "Yearly",
                    "source": "MarketWatch",
                    "revenue": 365820000000.0,
                    "cogs": 212980000000.0,
                    "cogs_excluding_deprecation_and_amortization": 201700000000.0,
                    "deprecation_and_amortization_expense": 11280000000.0,
                    "gross_profit": 152840000000.0,
                    "gross_profit_margin": 0.42,
                    "sga_expenses": 43890000000.0,
                    "research_and_development_expenses": 21910000000.0,
                    "unusual_expense": None,
                    "ebit": None,
                    "non_operating_income": 60000000.0,
                    "non_operating_interest_income": 2840000000.0,
                    "interest_expense": 2650000000.0,
                    "net_income_before_tax": 109210000000.0,
                    "income_tax": 14530000000.0,
                    "equity_in_affiliates": None,
                    "net_income_after_tax": None,
                    "other_after_tax_income": None,
                    "consolidated_net_income": 94680000000.0,
                    "minority_interest": None,
                    "net_income_before_extraordinaries": 94680000000.0,
                    "preferred_dividends": None,
                    "net_income_available_to_common": 94680000000.0,
                    "eps_basic": 5.67,
                    "basic_shares_outstanding": 16700000000.0,
                    "eps_diluted": 5.61,
                    "diluted_shares_outstanding": 16860000000.0,
                    "ebitda": 120230000000.0,
                    "net_income": 94680000000.0,
                    "deprecation_depletion_and_amortization": 11280000000.0,
                    "deprecation_depletion": 11280000000.0,
                    "amortization": None,
                    "deferred_taxes": None,
                    "investment_tax_credit": None,
                    "extraordinaries": None,
                    "changes_in_working_capital": -4910000000.0,
                    "accounts_receivables": -14030000000.0,
                    "accounts_payable": None,
                    "cash_from_operating_activities": 104040000000.0,
                    "capex": -11090000000.0,
                    "net_assets_from_acquisitions": -33000000.0,
                    "sale_of_fixed_assets_and_businesses": None,
                    "purchase_of_investments": -109690000000.0,
                    "sale_of_investments": 106870000000.0,
                    "cash_from_investing_activities": -14550000000.0,
                    "cash_dividends_paid": -14470000000.0,
                    "change_in_capital_stock": -84870000000.0,
                    "repurchase_of_common_and_preferred_stock": -85970000000.0,
                    "sale_of_common_and_preferred_stock": 1110000000.0,
                    "proceeds_from_stock_options": 1110000000.0,
                    "other_proceeds_from_sale_of_stock": None,
                    "change_in_debt": 12670000000.0,
                    "change_in_current_debt": 1020000000.0,
                    "change_in_long_term_debt": 11640000000.0,
                    "other_funds": -6690000000.0,
                    "cash_from_financing_activities": -93350000000.0,
                    "foreign_exchange_effect": None,
                    "miscellaneous_funds": None,
                    "net_change_in_cash": -3860000000.0,
                    "free_cash_flow": 92950000000.0,
                    "cash_and_short_term_investments": 62640000000.0,
                    "cash": 26910000000.0,
                    "short_term_investments": 35730000000.0,
                    "accounts_receivable": 51510000000.0,
                    "accounts_receivables_net": 26280000000.0,
                    "bad_debt_doubtful_accounts": None,
                    "other_receivable": 25230000000.0,
                    "accounts_receivable_turnover": 7.1,
                    "inventories": 6580000000.0,
                    "other_current_assets": 14110000000.0,
                    "total_current_assets": 134840000000.0,
                    "property_plant_equipment_net": 49530000000.0,
                    "property_plant_equipment_gross": 119810000000.0,
                    "buildings": 20040000000.0,
                    "land_and_improvements": None,
                    "computer_software_and_equipment": None,
                    "other_property_plant_equipment": 11020000000.0,
                    "accumulated_deprecation": 70280000000.0,
                    "total_investments_and_advances": 127880000000.0,
                    "long_term_note_receivables": None,
                    "intangible_assets": None,
                    "goodwill": None,
                    "other_intangibles": None,
                    "other_assets": 38760000000.0,
                    "total_assets": 351000000000.0,
                    "short_term_debt": 7450000000.0,
                    "current_portion_of_long_term_debt": 9690000000.0,
                    "accounts_payable_1": None,
                    "income_tax_payable": None,
                    "other_current_liabilities": 53580000000.0,
                    "total_current_liabilities": 125480000000.0,
                    "long_term_debt": 119380000000.0,
                    "provision_for_risks_and_charges": 24690000000.0,
                    "deferred_taxes_1": None,
                    "other_liabilities": 18360000000.0,
                    "deferred_income": None,
                    "total_liabilities": 287910000000.0,
                    "non_equity_reserves": None,
                    "preferred_stock": None,
                    "redeemable_preferred_stock": None,
                    "non_redeemable_preferred_stock": None,
                    "common_equity": 63090000000.0,
                    "retained_earnings": 5560000000.0,
                    "unrealized_gains_in_marketable_securities": None,
                    "treasury_stock": None,
                    "total_shareholders_equity": 63090000000.0,
                    "accumulated_minority_interest": None,
                    "total_equity": 63090000000.0,
                    "liabilities_and_shareholders_equity": 351000000000.0,
                }
            ],
        )
        symbol = "AAPL"
        frequency = "Yearly"
        year = 2021

        expected = [
            {
                "symbol": "AAPL",
                "year": 2021,
                "quarter": None,
                "name": "Apple",
                "inserted_at": None,
                "frequency": "Yearly",
                "source": "MarketWatch",
                "revenue": 365820000000.0,
                "cogs": 212980000000.0,
                "cogs_excluding_deprecation_and_amortization": 201700000000.0,
                "deprecation_and_amortization_expense": 11280000000.0,
                "gross_profit": 152840000000.0,
                "gross_profit_margin": 0.42,
                "sga_expenses": 43890000000.0,
                "research_and_development_expenses": 21910000000.0,
                "unusual_expense": None,
                "ebit": None,
                "non_operating_income": 60000000.0,
                "non_operating_interest_income": 2840000000.0,
                "interest_expense": 2650000000.0,
                "net_income_before_tax": 109210000000.0,
                "income_tax": 14530000000.0,
                "equity_in_affiliates": None,
                "net_income_after_tax": None,
                "other_after_tax_income": None,
                "consolidated_net_income": 94680000000.0,
                "minority_interest": None,
                "net_income_before_extraordinaries": 94680000000.0,
                "preferred_dividends": None,
                "net_income_available_to_common": 94680000000.0,
                "eps_basic": 5.67,
                "basic_shares_outstanding": 16700000000.0,
                "eps_diluted": 5.61,
                "diluted_shares_outstanding": 16860000000.0,
                "ebitda": 120230000000.0,
                "net_income": 94680000000.0,
                "deprecation_depletion_and_amortization": 11280000000.0,
                "deprecation_depletion": 11280000000.0,
                "amortization": None,
                "deferred_taxes": None,
                "investment_tax_credit": None,
                "extraordinaries": None,
                "changes_in_working_capital": -4910000000.0,
                "accounts_receivables": -14030000000.0,
                "accounts_payable": None,
                "cash_from_operating_activities": 104040000000.0,
                "capex": -11090000000.0,
                "net_assets_from_acquisitions": -33000000.0,
                "sale_of_fixed_assets_and_businesses": None,
                "purchase_of_investments": -109690000000.0,
                "sale_of_investments": 106870000000.0,
                "cash_from_investing_activities": -14550000000.0,
                "cash_dividends_paid": -14470000000.0,
                "change_in_capital_stock": -84870000000.0,
                "repurchase_of_common_and_preferred_stock": -85970000000.0,
                "sale_of_common_and_preferred_stock": 1110000000.0,
                "proceeds_from_stock_options": 1110000000.0,
                "other_proceeds_from_sale_of_stock": None,
                "change_in_debt": 12670000000.0,
                "change_in_current_debt": 1020000000.0,
                "change_in_long_term_debt": 11640000000.0,
                "other_funds": -6690000000.0,
                "cash_from_financing_activities": -93350000000.0,
                "foreign_exchange_effect": None,
                "miscellaneous_funds": None,
                "net_change_in_cash": -3860000000.0,
                "free_cash_flow": 92950000000.0,
                "cash_and_short_term_investments": 62640000000.0,
                "cash": 26910000000.0,
                "short_term_investments": 35730000000.0,
                "accounts_receivable": 51510000000.0,
                "accounts_receivables_net": 26280000000.0,
                "bad_debt_doubtful_accounts": None,
                "other_receivable": 25230000000.0,
                "accounts_receivable_turnover": 7.1,
                "inventories": 6580000000.0,
                "other_current_assets": 14110000000.0,
                "total_current_assets": 134840000000.0,
                "property_plant_equipment_net": 49530000000.0,
                "property_plant_equipment_gross": 119810000000.0,
                "buildings": 20040000000.0,
                "land_and_improvements": None,
                "computer_software_and_equipment": None,
                "other_property_plant_equipment": 11020000000.0,
                "accumulated_deprecation": 70280000000.0,
                "total_investments_and_advances": 127880000000.0,
                "long_term_note_receivables": None,
                "intangible_assets": None,
                "goodwill": None,
                "other_intangibles": None,
                "other_assets": 38760000000.0,
                "total_assets": 351000000000.0,
                "short_term_debt": 7450000000.0,
                "current_portion_of_long_term_debt": 9690000000.0,
                "accounts_payable_1": None,
                "income_tax_payable": None,
                "other_current_liabilities": 53580000000.0,
                "total_current_liabilities": 125480000000.0,
                "long_term_debt": 119380000000.0,
                "provision_for_risks_and_charges": 24690000000.0,
                "deferred_taxes_1": None,
                "other_liabilities": 18360000000.0,
                "deferred_income": None,
                "total_liabilities": 287910000000.0,
                "non_equity_reserves": None,
                "preferred_stock": None,
                "redeemable_preferred_stock": None,
                "non_redeemable_preferred_stock": None,
                "common_equity": 63090000000.0,
                "retained_earnings": 5560000000.0,
                "unrealized_gains_in_marketable_securities": None,
                "treasury_stock": None,
                "total_shareholders_equity": 63090000000.0,
                "accumulated_minority_interest": None,
                "total_equity": 63090000000.0,
                "liabilities_and_shareholders_equity": 351000000000.0,
            }
        ]

        # when
        with mock.patch(
            "eetc_data_client.client.EETCDataClient._send_http_request",
            return_value=mock_response,
        ):
            data = self.eetc_data_client.get_fundamentals_data(
                symbol, frequency, year, as_json=True
            )

        # then
        self.assertEqual(expected, data)

    def test_get_macroeconomic_data_as_json(self):
        # given
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json = MagicMock(
            return_value=[
                {
                    "year": 2020,
                    "quarter": None,
                    "month": None,
                    "week": None,
                    "date": "2020-01-01T00:00:00Z",
                    "name": "US Real GDP",
                    "value": -3.4,
                    "inserted_at": None,
                    "frequency": "Yearly",
                }
            ]
        )
        name = "US Real GDP"
        frequency = "Yearly"
        from_date = "2020-01-01"
        to_date = "2020-12-30"

        expected = [
            {
                "year": 2020,
                "quarter": None,
                "month": None,
                "week": None,
                "date": "2020-01-01T00:00:00Z",
                "name": "US Real GDP",
                "value": -3.4,
                "inserted_at": None,
                "frequency": "Yearly",
            }
        ]

        # when
        with mock.patch(
            "eetc_data_client.client.EETCDataClient._send_http_request",
            return_value=mock_response,
        ):
            data = self.eetc_data_client.get_macroeconomic_data(
                name, frequency, from_date, to_date, as_json=True
            )

        # then
        self.assertEqual(expected, data)

    def test__send_http_request(self):
        # given
        # when
        # then
        pass
