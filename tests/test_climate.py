"""Tests for backwards compatibility module."""

from noaa.climate import API, NOAA
from noaa.client import NOAA as ClientNOAA


class TestBackwardsCompatibility:
    """Tests for backwards compatibility."""

    def test_api_alias(self):
        """API should be alias for NOAA."""
        assert API is NOAA

    def test_noaa_is_client_noaa(self):
        """NOAA should be the client NOAA class."""
        assert NOAA is ClientNOAA

    def test_can_create_client_with_api(self):
        """Should be able to create client using API alias."""
        client = API("test-token")
        assert isinstance(client, ClientNOAA)
