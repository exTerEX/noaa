"""Custom exceptions for the NOAA API client."""


class NOAAException(Exception):
    """Base exception for NOAA API errors."""

    pass


class ValidationError(NOAAException):
    """Raised when input validation fails."""

    pass


class APIError(NOAAException):
    """Raised when the API returns an error."""

    pass
