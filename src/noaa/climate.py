"""Backwards compatibility module - use noaa.client instead."""

from .client import NOAA

# Alias for backwards compatibility
API = NOAA

__all__ = ["API", "NOAA"]
