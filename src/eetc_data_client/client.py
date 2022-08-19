from typing import Union, List, Dict

import pandas as pd
import requests
from requests import Response


class EETCDataClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://eetc-data-hub-service-nb7ewdzv6q-ue.a.run.app/api"
        # TODO check API Key validity during __init__ & raise exception

    def _send_http_request(self, url: str, params: dict) -> Response:
        response = requests.get(
            url,
            params=params,
            headers={"EETC-API-Key": self.api_key},
        )

        if response.status_code != 200:
            response.raise_for_status()

        return response

    def get_price_data(
        self,
        symbol: str,
        date: str = None,
        from_date: str = None,
        to_date: str = None,
        as_json=False,
    ) -> Union[pd.DataFrame, List[Dict]]:
        """
        Get historical Price data from EETC Data Hub via REST API.

        :param symbol: Symbol of the instrument.
        :param date: Specific date in string format "yyyy-mm-dd"
        :param from_date: Earliest date in string format "yyyy-mm-dd"
        :param to_date: Latest date in string format "yyyy-mm-dd"
        :param as_json: Indicates if caller wants data returned as JSON. False
        by default, if False, it will return the data as a pandas DataFrame.
        :return: Historical Price data as a pandas DataFrame.
        """

        url = f"{self.base_url}/price/?symbol={symbol}"
        params = {}

        # add optional query params
        if date:
            params["date"] = date

        if from_date:
            params["from_date"] = from_date

        if to_date:
            params["to_date"] = to_date

        # send the HTTP request to EETC Data Hub
        response = self._send_http_request(url, params)

        # process and return response data
        response_data = response.json()

        if as_json:
            return response_data

        df = pd.json_normalize(response_data)
        df = df.sort_values(by=["date"])

        return df

    def get_fundamentals_data(
        self,
        symbol: str,
        frequency: str = "Quarterly",
        name: str = None,
        year: int = None,
        as_json=False,
    ) -> Union[pd.DataFrame, List[Dict]]:
        """
        Get historical Fundamentals data from EETC Data Hub via REST API.

        :param symbol: Symbol of the instrument.
        :param frequency: Can be "Yearly" or "Quarterly".
        :param name: Name of the instrument/company.
        :param year: Specific year for which the caller wants data.
        :param as_json: Indicates if caller wants data returned as JSON. False
        by default, if False, it will return the data as a pandas DataFrame.
        :return: Historical Fundamentals data as a pandas DataFrame.
        """

        url = f"{self.base_url}/fundamentals/?symbol={symbol}&frequency={frequency}"
        params = {}

        # add optional query params
        if name:
            params["name"] = name

        if year:
            params["year"] = year

        # send the HTTP request to EETC Data Hub
        response = self._send_http_request(url, params)

        # process and return response data
        response_data = response.json()

        if as_json:
            return response_data

        return pd.json_normalize(response_data)

    def get_macroeconomic_data(
        self,
        name: str,
        frequency: str = None,
        from_date: str = None,
        to_date: str = None,
        month: int = None,
        quarter: int = None,
        as_json=False,
    ) -> Union[pd.DataFrame, List[Dict]]:
        """
        Get historical Macroeconomic data from EETC Data Hub via REST API.

        :param name: Name of the macroeconomic data point.
        :param frequency: "Yearly", "Quarterly", "Monthly", "Weekly", "Daily".
        :param from_date: Earliest date in string format "yyyy-mm-dd"
        :param to_date: Latest date in string format "yyyy-mm-dd"
        :param month: Specific month for which the caller wants data.
        :param quarter: Specific quarter for which the caller wants data.
        :param as_json: Indicates if caller wants data returned as JSON. False
        by default, if False, it will return the data as a pandas DataFrame.
        :return: Historical Macroeconomic data as a pandas DataFrame.
        """

        url = f"{self.base_url}/macroeconomic/?name={name}"
        params = {}

        # add optional query params
        if frequency:
            params["frequency"] = frequency

        if from_date:
            params["from_date"] = from_date

        if to_date:
            params["to_date"] = to_date

        if month:
            params["month"] = month

        if quarter:
            params["quarter"] = quarter

        # send the HTTP request to EETC Data Hub
        response = self._send_http_request(url, params)

        # process and return response data
        response_data = response.json()

        if as_json:
            return response_data

        return pd.json_normalize(response_data)
