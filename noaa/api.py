"""
Source code for API implementation

MIT License

Copyright (c) 2022 Andreas Sagen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

__author__ = "Andreas Sagen"
__copyright__ = ""
__licence__ = "MIT"
__version__ = "0.0.1a0"

import json
import urllib.parse
import urllib.request
from typing import Optional


class NOAA:
    """Class for interfacing with NOAA climate data API

        :param key: Access token from NOAA
        :type key: str
    """

    def __init__(self, key: str):
        self._api_header = {
            "token": key
        }
        self._host = "https://www.ncdc.noaa.gov/cdo-web/api/v2/"

    def get_datasets(
        self,
        dataset_id: Optional[str] = None,
        data_type_id: Optional[str] = None,
        location_id: Optional[str] = None,
        station_id: Optional[str] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        sort_field: Optional[str] = None,
        sort_order: Optional[str] = "asc",
        limit: Optional[int] = 25,
        offset: Optional[int] = 0
    ) -> dict:
        """Get list of available datasets in CDO or info on a specific dataset

        :param dataset_id: Identification to dataset in CDO, defaults to None
        :type dataset_id: str, optional
        :param data_type_id: Identification to datatype(s) in CDO, defaults to None
        :type data_type_id: str, optional
        :param location_id: Identification to location(s) in CDO, defaults to None
        :type location_id: str, optional
        :param station_id: Identification to station(s) in CDO, defaults to None
        :type station_id: str, optional
        :param start_date: Filter from time in ISO formatted date, defaults to None
        :type start_date: str, optional
        :param end_date: Filter to time in ISO formatted date, defaults to None
        :type end_date: str, optional
        :param sort_field: Field to be used when sorting, defaults to None
        :type sort_field: str, optional
        :param sort_order: Which order to sort by, defaults to "asc"
        :type sort_order: str, optional
        :param limit: Limit number of results in the response from CDO, defaults to 25
        :type limit: int, optional
        :param offset: Offset first result in response from CDO, defaults to 0
        :type offset: int, optional

        :return: Return a object with data from response
        :rtype: dict
        """

        endpoint = "datasets"
        if dataset_id is not None:
            endpoint += f"/{dataset_id}"

        return self._call_api(
            endpoint=endpoint,
            data_type_id=data_type_id,
            end_date=end_date,
            limit=limit,
            location_id=location_id,
            offset=offset,
            sort_field=sort_field,
            sort_order=sort_order,
            start_date=start_date,
            station_id=station_id
        )

    def get_data_categories(
        self,
        category_id: Optional[str] = None,
        dataset_id: Optional[str] = None,
        location_id: Optional[str] = None,
        station_id: Optional[str] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        sort_field: Optional[str] = None,
        sort_order: Optional[str] = "asc",
        limit: Optional[int] = 25,
        offset: Optional[int] = 0
    ) -> dict:
        """Get list of available categories in CDO or info on a specific category

        :param category_id: Identification to category in CDO, defaults to None
        :type category_id: str, optional
        :param dataset_id: Identification to dataset(s) in CDO, defaults to None
        :type dataset_id: str, optional
        :param location_id: Identification to location(s) in CDO, defaults to None
        :type location_id: str, optional
        :param station_id: Identification to station(s) in CDO, defaults to None
        :type station_id: str, optional
        :param start_date: Filter from time in ISO formatted date, defaults to None
        :type start_date: str, optional
        :param end_date: Filter to time in ISO formatted date, defaults to None
        :type end_date: str, optional
        :param sort_field: Field to be used when sorting, defaults to None
        :type sort_field: str, optional
        :param sort_order: Which order to sort by, defaults to "asc"
        :type sort_order: str, optional
        :param limit: Limit number of results in the response from CDO, defaults to 25
        :type limit: int, optional
        :param offset: Offset first result in response from CDO, defaults to 0
        :type offset: int, optional

        :return: Return a object with data from response
        :rtype: dict
        """

        endpoint = "datacategories"
        if category_id is not None:
            endpoint += f"/{category_id}"

        return self._call_api(
            endpoint=endpoint,
            dataset_id=dataset_id,
            end_date=end_date,
            limit=limit,
            location_id=location_id,
            offset=offset,
            sort_field=sort_field,
            sort_order=sort_order,
            start_date=start_date,
            station_id=station_id
        )

    def get_data_types(
        self,
        type_id: Optional[str] = None,
        dataset_id: Optional[str] = None,
        location_id: Optional[str] = None,
        station_id: Optional[str] = None,
        data_category_id: Optional[str] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        sort_field: Optional[str] = None,
        sort_order: Optional[str] = "asc",
        limit: Optional[int] = 25,
        offset: Optional[int] = 0
    ) -> dict:
        """Get list of available datatypes in CDO or info on a specific datatype

        :param type_id: Identification to type in CDO, defaults to None
        :type type_id: str, optional
        :param dataset_id: Identification to dataset(s) in CDO, defaults to None
        :type dataset_id: str, optional
        :param location_id: Identification to location(s) in CDO, defaults to None
        :type location_id: str, optional
        :param station_id: Identification to station(s) in CDO, defaults to None
        :type station_id: str, optional
        :param data_category_id: Identification to data category in CDO, defaults to None
        :type data_category_id: str, optional
        :param start_date: Filter from time in ISO formatted date, defaults to None
        :type start_date: str, optional
        :param end_date: Filter to time in ISO formatted date, defaults to None
        :type end_date: str, optional
        :param sort_field: Field to be used when sorting, defaults to None
        :type sort_field: str, optional
        :param sort_order: Which order to sort by, defaults to "asc"
        :type sort_order: str, optional
        :param limit: Limit number of results in the response from CDO, defaults to 25
        :type limit: int, optional
        :param offset: Offset first result in response from CDO, defaults to 0
        :type offset: int, optional

        :return: Return a object with data from response
        :rtype: dict
        """

        endpoint = "datatypes"
        if type_id is not None:
            endpoint += f"/{type_id}"

        return self._call_api(
            endpoint=endpoint,
            dataset_id=dataset_id,
            end_date=end_date,
            limit=limit,
            location_id=location_id,
            offset=offset,
            sort_field=sort_field,
            sort_order=sort_order,
            start_date=start_date,
            station_id=station_id,
            data_category_id=data_category_id
        )

    def get_location_categories(
        self,
        location_category_id: Optional[str] = None,
        dataset_id: Optional[str] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        sort_field: Optional[str] = None,
        sort_order: Optional[str] = "asc",
        limit: Optional[int] = 25,
        offset: Optional[int] = 0
    ) -> dict:
        """Get list of available location categories in CDO or info on a specific location category

        :param location_category_id: Identification to location category in CDO, defaults to None
        :type location_category_id: str, optional
        :param dataset_id: Identification to dataset(s) in CDO, defaults to None
        :type dataset_id: str, optional
        :param start_date: Filter from time in ISO formatted date, defaults to None
        :type start_date: str, optional
        :param end_date: Filter to time in ISO formatted date, defaults to None
        :type end_date: str, optional
        :param sort_field: Field to be used when sorting, defaults to None
        :type sort_field: str, optional
        :param sort_order: Which order to sort by, defaults to "asc"
        :type sort_order: str, optional
        :param limit: Limit number of results in the response from CDO, defaults to 25
        :type limit: int, optional
        :param offset: Offset first result in response from CDO, defaults to 0
        :type offset: int, optional

        :return: Return a object with data from response
        :rtype: dict
        """

        endpoint = "locationcategories"
        if location_category_id is not None:
            endpoint += f"/{location_category_id}"

        return self._call_api(
            endpoint=endpoint,
            dataset_id=dataset_id,
            end_date=end_date,
            limit=limit,
            offset=offset,
            sort_field=sort_field,
            sort_order=sort_order,
            start_date=start_date
        )

    def get_locations(
        self,
        location_id: Optional[str] = None,
        dataset_id: Optional[str] = None,
        location_category_id: Optional[str] = None,
        data_category_id: Optional[str] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        sort_field: Optional[str] = None,
        sort_order: Optional[str] = "asc",
        limit: Optional[int] = 25,
        offset: Optional[int] = 0
    ) -> dict:
        """Get list of available locations in CDO or info on a specific location

        :param location_id: Identification to location in CDO, defaults to None
        :type location_id: str, optional
        :param dataset_id: Identification to dataset(s) in CDO, defaults to None
        :type dataset_id: str, optional
        :param location_category_id: Identification to location category in CDO, defaults to None
        :type location_category_id: str, optional
        :param data_category_id: Identification to data category in CDO, defaults to None
        :type data_category_id: str, optional
        :param start_date: Filter from time in ISO formatted date, defaults to None
        :type start_date: str, optional
        :param end_date: Filter to time in ISO formatted date, defaults to None
        :type end_date: str, optional
        :param sort_field: Field to be used when sorting, defaults to None
        :type sort_field: str, optional
        :param sort_order: Which order to sort by, defaults to "asc"
        :type sort_order: str, optional
        :param limit: Limit number of results in the response from CDO, defaults to 25
        :type limit: int, optional
        :param offset: Offset first result in response from CDO, defaults to 0
        :type offset: int, optional

        :return: Return a object with data from response
        :rtype: dict
        """

        endpoint = "locations"
        if location_id is not None:
            endpoint += f"/{location_id}"

        return self._call_api(
            endpoint=endpoint,
            data_category_id=data_category_id,
            dataset_id=dataset_id,
            end_date=end_date,
            limit=limit,
            location_category_id=location_category_id,
            offset=offset,
            sort_field=sort_field,
            sort_order=sort_order,
            start_date=start_date
        )

    def get_stations(
        self,
        station_id: Optional[str] = None,
        dataset_id: Optional[str] = None,
        location_id: Optional[str] = None,
        data_category_id: Optional[str] = None,
        data_type_id: Optional[str] = None,
        extent: Optional[str] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        sort_field: Optional[str] = None,
        sort_order: Optional[str] = "asc",
        limit: Optional[int] = 25,
        offset: Optional[int] = 0
    ) -> dict:
        """Get list of available stations in CDO or info on a specific station

        :param station_id: Identification to station in CDO, defaults to None
        :type station_id: str, optional
        :param dataset_id: Identification to dataset(s) in CDO, defaults to None
        :type dataset_id: str, optional
        :param location_id: Identification to location(s) in CDO, defaults to None
        :type location_id: str, optional
        :param data_category_id: Identification to data category in CDO, defaults to None
        :type data_category_id: str, optional
        :param data_type_id: Identification to datatype(s) in CDO, defaults to None
        :type data_type_id: str, optional
        :param extent: Desired geographical extent for search in CDO, defaults to None
        :type extent: str, optional
        :param start_date: Filter from time in ISO formatted date, defaults to None
        :type start_date: str, optional
        :param end_date: Filter to time in ISO formatted date, defaults to None
        :type end_date: str, optional
        :param sort_field: Field to be used when sorting, defaults to None
        :type sort_field: str, optional
        :param sort_order: Which order to sort by, defaults to "asc"
        :type sort_order: str, optional
        :param limit: Limit number of results in the response from CDO, defaults to 25
        :type limit: int, optional
        :param offset: Offset first result in response from CDO, defaults to 0
        :type offset: int, optional

        :return: Return a object with data from response
        :rtype: dict
        """

        endpoint = "stations"
        if station_id is not None:
            endpoint += f"/{station_id}"

        return self._call_api(
            endpoint=endpoint,
            data_category_id=data_category_id,
            dataset_id=dataset_id,
            data_type_id=data_type_id,
            end_date=end_date,
            extent=extent,
            limit=limit,
            start_date=start_date,
            location_id=location_id,
            offset=offset,
            sort_field=sort_field,
            sort_order=sort_order
        )

    # FIXME: problem in this function
    def get_data(
        self,
        dataset_id: str,
        data_type_id: Optional[str] = None,
        location_id: Optional[str] = None,
        station_id: Optional[str] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        units: Optional[str] = "metric",
        sort_field: Optional[str] = None,
        sort_order: Optional[str] = "asc",
        limit: Optional[int] = 25,
        offset: Optional[int] = 0,
        include_metadata: Optional[bool] = False
    ) -> dict:
        """Get available data in CDO

        :param dataset_id: Identification to dataset in CDO
        :type dataset_id: str
        :param data_type_id: Identification to datatype(s) in CDO, defaults to None
        :type data_type_id: str, optional
        :param location_id: Identification to location(s) in CDO, defaults to None
        :type location_id: str, optional
        :param station_id: Identification to station(s) in CDO, defaults to None
        :type station_id: str, optional
        :param start_date: Filter from time in ISO formatted date, defaults to None
        :type start_date: str, optional
        :param end_date: Filter to time in ISO formatted date, defaults to None
        :type end_date: str, optional
        :param units: Data will be scaled and converted to the specified units, defaults to "metric"
        :type units: str, optional
        :param sort_field: Field to be used when sorting, defaults to None
        :type sort_field: str, optional
        :param sort_order: Which order to sort by, defaults to "asc"
        :type sort_order: str, optional
        :param limit: Limit number of results in the response from CDO, defaults to 25
        :type limit: int, optional
        :param offset: Offset first result in response from CDO, defaults to 0
        :type offset: int, optional
        :param include_metadata: Include or exclude metadata from CDO, defaults to False
        :type include_metadata: bool, optional

        :return: Return a object with data from response
        :rtype: dict
        """

        return self._call_api(
            endpoint="data",
            data_type_id=data_type_id,
            dataset_id=dataset_id,
            end_date=end_date,
            include_metadata=include_metadata,
            limit=limit,
            location_id=location_id,
            offset=offset,
            sort_field=sort_field,
            sort_order=sort_order,
            start_date=start_date,
            station_id=station_id,
            units=units
        )

    def _call_api(
        self,
        endpoint: str,
        dataset_id: Optional[str] = None,
        data_type_id: Optional[str] = None,
        data_category_id: Optional[str] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        extent: Optional[str] = None,
        include_metadata: Optional[bool] = False,
        limit: Optional[int] = 25,
        location_id: Optional[str] = None,
        location_category_id: Optional[str] = None,
        offset: Optional[int] = 0,
        sort_field: Optional[str] = None,
        sort_order: Optional[str] = "asc",
        station_id: Optional[str] = None,
        units: Optional[str] = "metric"
    ) -> dict:

        data = {
            "datacategoryid": data_category_id,
            "datasetid": dataset_id,
            "datatypeid": data_type_id,
            "enddate": end_date,
            "extent": extent,
            "includemetadata": include_metadata,
            "limit": limit,
            "locationcategoryid": location_category_id,
            "locationid": location_id,
            "offset": offset,
            "sortfield": sort_field,
            "sortorder": sort_order,
            "startdate": start_date,
            "stationid": station_id,
            "units": units
        }

        data = {key: val for key, val in data.items() if val is not None}

        url = urllib.parse.urljoin(self._host, endpoint)
        params = urllib.parse.urlencode(data)

        request = urllib.request.Request(
            url="?".join([url, params]),
            headers=self._api_header, method="GET")

        with urllib.request.urlopen(request) as response:
            return json.loads(response.read())