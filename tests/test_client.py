import unittest
from unittest import mock
from unittest.mock import MagicMock

import pandas as pd
from pandas._testing import assert_frame_equal

from eetc_data_client.client import EETCDataClient


class TestEETCDataClient(unittest.TestCase):
    def assertDataFrameEqual(self, a, b, msg):
        try:
            assert_frame_equal(a, b)
        except AssertionError as e:
            raise self.failureException(msg) from e

    def setUp(self):
        self.addTypeEqualityFunc(pd.DataFrame, self.assertDataFrameEqual)
        self.client = EETCDataClient("test_api_key")

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
            data = self.client.get_price_data(symbol)

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
            data = self.client.get_price_data(symbol, as_json=True)

        # then
        self.assertEqual(expected, data)

    def test_get_fundamentals_data(self):
        raise NotImplementedError()

    def test_get_macroeconomic_data(self):
        raise NotImplementedError()

    def test_get_fundamentals_data_as_json(self):
        raise NotImplementedError()

    def test_get_macroeconomic_data_as_json(self):
        raise NotImplementedError()

    def test__send_http_request(self):
        raise NotImplementedError()
