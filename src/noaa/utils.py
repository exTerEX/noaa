"""Utility functions for the NOAA API client."""

import datetime
import json
import urllib.parse
import urllib.request
from typing import Any, Dict, Optional, Sequence, Union

from .exceptions import ValidationError


def parse_date(
    date_value: Optional[Union[str, datetime.datetime]],
    name: str,
    include_time: bool = False,
) -> Optional[str]:
    """Parse and format a date value for the API.

    :param date_value: Date as string or datetime object
    :param name: Name of the parameter (for error messages)
    :param include_time: Whether to include time component
    :return: Formatted date string or None
    """
    if date_value is None:
        return None

    if isinstance(date_value, datetime.datetime):
        dt = date_value
    elif isinstance(date_value, str):
        try:
            dt = datetime.datetime.fromisoformat(date_value)
        except ValueError as error:
            raise ValidationError(
                f"{name} must be in ISO date format"
            ) from error
    else:
        raise ValidationError(f"{name} must be a string or datetime object")

    if include_time:
        return dt.strftime("%Y-%m-%dT%H:%M:%S")
    return dt.strftime("%Y-%m-%d")


def join_ids(value: Optional[Union[str, Sequence[str]]]) -> Optional[str]:
    """Join a sequence of IDs into an ampersand-separated string.

    :param value: Single ID or sequence of IDs
    :return: Joined string or original value
    """
    if isinstance(value, (list, tuple)):
        return "&".join(value)
    if isinstance(value, str) or value is None:
        return value
    return str(value)


def build_query_params(params: Dict[str, Any]) -> str:
    """Build URL query parameters from a dictionary.

    :param params: Dictionary of parameter names and values
    :return: URL-encoded query string
    """
    # Filter out None values
    filtered = {
        key: value for key, value in params.items() if value is not None
    }

    # URL encode, preserving ampersands in joined IDs
    encoded = urllib.parse.urlencode(filtered, safe="")
    return encoded.replace("%26", "&")


def make_api_request(url: str, headers: Dict[str, str]) -> dict:
    """Make a GET request to the API.

    :param url: Full URL including query parameters
    :param headers: Request headers
    :return: Parsed JSON response
    """
    request = urllib.request.Request(url=url, headers=headers, method="GET")

    with urllib.request.urlopen(request) as response:
        return json.loads(response.read())
