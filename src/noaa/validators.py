"""Input validation functions for the NOAA API client."""

from typing import Any, Optional

from .exceptions import ValidationError


VALID_SORT_FIELDS = frozenset(
    [None, "id", "name", "mindate", "maxdate", "datacoverage"]
)
VALID_SORT_ORDERS = frozenset(["asc", "desc"])
VALID_UNITS = frozenset(["standard", "metric"])


def validate_string_or_none(value: Any, name: str) -> None:
    """Validate that a value is a string or None."""
    if not isinstance(value, str) and value is not None:
        raise ValidationError(f"{name} should be a string")


def validate_string_or_sequence(value: Any, name: str) -> None:
    """Validate that a value is a string, sequence of strings, or None."""
    if value is None:
        return

    if isinstance(value, str):
        return

    if isinstance(value, (list, tuple)):
        for item in value:
            if not isinstance(item, str):
                raise ValidationError(
                    f"All values in {name} should be strings"
                )
        return

    raise ValidationError(f"{name} should be a string or sequence of strings")


def validate_limit(limit: int) -> None:
    """Validate the limit parameter."""
    if not isinstance(limit, int):
        raise ValidationError("limit should be an integer")
    if limit < 0 or limit > 1000:
        raise ValidationError("limit must be between 0 and 1000")


def validate_offset(offset: int) -> None:
    """Validate the offset parameter."""
    if not isinstance(offset, int):
        raise ValidationError("offset should be an integer")


def validate_sort_field(sort_field: Optional[str]) -> None:
    """Validate the sort_field parameter."""
    if sort_field is not None and not isinstance(sort_field, str):
        raise ValidationError("sort_field should be a string")
    if sort_field not in VALID_SORT_FIELDS:
        raise ValidationError(
            f"sort_field must be one of: {', '.join(str(f) for f in VALID_SORT_FIELDS)}"
        )


def validate_sort_order(sort_order: str) -> None:
    """Validate the sort_order parameter."""
    if not isinstance(sort_order, str):
        raise ValidationError("sort_order should be a string")
    if sort_order not in VALID_SORT_ORDERS:
        raise ValidationError(
            f"sort_order must be one of: {', '.join(VALID_SORT_ORDERS)}"
        )


def validate_units(units: str) -> None:
    """Validate the units parameter."""
    if not isinstance(units, str):
        raise ValidationError("units should be a string")
    if units not in VALID_UNITS:
        raise ValidationError(
            f"units must be one of: {', '.join(VALID_UNITS)}"
        )


def validate_boolean(value: Any, name: str) -> None:
    """Validate that a value is a boolean."""
    if not isinstance(value, bool):
        raise ValidationError(f"{name} should be a boolean")
