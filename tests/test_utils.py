"""Tests for utility functions."""

import datetime
import pytest
from unittest.mock import MagicMock, patch

from noaa.utils import parse_date, join_ids, build_query_params, make_api_request
from noaa.exceptions import ValidationError


class TestParseDate:
    """Tests for parse_date function."""

    def test_none_value(self):
        """Should return None for None input."""
        assert parse_date(None, "date") is None

    def test_valid_date_string(self):
        """Should parse valid ISO date strings."""
        result = parse_date("2023-01-15", "date")
        assert result == "2023-01-15"

    def test_valid_datetime_string(self):
        """Should parse valid ISO datetime strings."""
        result = parse_date("2023-01-15T10:30:00", "date")
        assert result == "2023-01-15"

    def test_valid_datetime_with_time(self):
        """Should include time when requested."""
        result = parse_date("2023-01-15T10:30:00", "date", include_time=True)
        assert result == "2023-01-15T10:30:00"

    def test_datetime_object(self):
        """Should accept datetime objects."""
        dt = datetime.datetime(2023, 1, 15, 10, 30, 0)
        result = parse_date(dt, "date")
        assert result == "2023-01-15"

    def test_datetime_object_with_time(self):
        """Should include time from datetime objects when requested."""
        dt = datetime.datetime(2023, 1, 15, 10, 30, 45)
        result = parse_date(dt, "date", include_time=True)
        assert result == "2023-01-15T10:30:45"

    def test_invalid_format(self):
        """Should raise error for invalid date format."""
        with pytest.raises(ValidationError, match="ISO date format"):
            parse_date("01-15-2023", "date")

    def test_invalid_type(self):
        """Should raise error for invalid type."""
        with pytest.raises(ValidationError, match="string or datetime"):
            parse_date(123, "date")  # type: ignore


class TestJoinIds:
    """Tests for join_ids function."""

    def test_none_value(self):
        """Should return None for None input."""
        assert join_ids(None) is None

    def test_string_value(self):
        """Should return string unchanged."""
        assert join_ids("GHCND") == "GHCND"

    def test_list_value(self):
        """Should join list with ampersands."""
        result = join_ids(["GHCND", "GSOM", "GSOY"])
        assert result == "GHCND&GSOM&GSOY"

    def test_tuple_value(self):
        """Should join tuple with ampersands."""
        result = join_ids(("GHCND", "GSOM"))
        assert result == "GHCND&GSOM"

    def test_empty_list(self):
        """Should return empty string for empty list."""
        assert join_ids([]) == ""


class TestBuildQueryParams:
    """Tests for build_query_params function."""

    def test_empty_params(self):
        """Should return empty string for empty dict."""
        assert build_query_params({}) == ""

    def test_filters_none_values(self):
        """Should filter out None values."""
        params = {"a": "1", "b": None, "c": "3"}
        result = build_query_params(params)
        assert "a=1" in result
        assert "c=3" in result
        assert "b" not in result

    def test_encodes_special_characters(self):
        """Should URL encode special characters."""
        params = {"location": "NY US"}
        result = build_query_params(params)
        assert "location=NY+US" in result or "location=NY%20US" in result

    def test_preserves_ampersands(self):
        """Should preserve ampersands in values."""
        params = {"ids": "A&B&C"}
        result = build_query_params(params)
        assert "ids=A&B&C" in result


class TestMakeApiRequest:
    """Tests for make_api_request function."""

    def test_successful_request(self, mock_response):
        """Should return parsed JSON response."""
        expected_data = {"results": [1, 2, 3]}
        mock = mock_response(expected_data)

        with patch("noaa.utils.urllib.request.urlopen", return_value=mock):
            result = make_api_request("http://test.com", {"token": "abc"})

        assert result == expected_data

    def test_request_headers(self, mock_response):
        """Should pass headers to request."""
        mock = mock_response({"results": []})

        with patch("noaa.utils.urllib.request.urlopen", return_value=mock):
            with patch("noaa.utils.urllib.request.Request") as mock_request:
                mock_request.return_value = MagicMock()
                make_api_request("http://test.com", {"token": "abc"})

                mock_request.assert_called_once()
                call_kwargs = mock_request.call_args[1]
                assert call_kwargs["headers"] == {"token": "abc"}
                assert call_kwargs["method"] == "GET"
