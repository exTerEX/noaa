"""Tests for validation functions."""

import pytest
from noaa.validators import (
    validate_string_or_none,
    validate_string_or_sequence,
    validate_limit,
    validate_offset,
    validate_sort_field,
    validate_sort_order,
    validate_units,
    validate_boolean,
)
from noaa.exceptions import ValidationError


class TestValidateStringOrNone:
    """Tests for validate_string_or_none."""

    def test_valid_string(self):
        """Should accept valid strings."""
        validate_string_or_none("test", "param")

    def test_valid_none(self):
        """Should accept None."""
        validate_string_or_none(None, "param")

    def test_invalid_int(self):
        """Should reject integers."""
        with pytest.raises(ValidationError, match="should be a string"):
            validate_string_or_none(123, "param")

    def test_invalid_list(self):
        """Should reject lists."""
        with pytest.raises(ValidationError, match="should be a string"):
            validate_string_or_none(["a", "b"], "param")


class TestValidateStringOrSequence:
    """Tests for validate_string_or_sequence."""

    def test_valid_string(self):
        """Should accept valid strings."""
        validate_string_or_sequence("test", "param")

    def test_valid_none(self):
        """Should accept None."""
        validate_string_or_sequence(None, "param")

    def test_valid_list(self):
        """Should accept list of strings."""
        validate_string_or_sequence(["a", "b", "c"], "param")

    def test_valid_tuple(self):
        """Should accept tuple of strings."""
        validate_string_or_sequence(("a", "b"), "param")

    def test_invalid_list_with_int(self):
        """Should reject list containing non-strings."""
        with pytest.raises(ValidationError, match="should be strings"):
            validate_string_or_sequence(["a", 123], "param")

    def test_invalid_int(self):
        """Should reject integers."""
        with pytest.raises(ValidationError, match="should be a string or sequence"):
            validate_string_or_sequence(123, "param")


class TestValidateLimit:
    """Tests for validate_limit."""

    def test_valid_limit(self):
        """Should accept valid limits."""
        validate_limit(25)
        validate_limit(0)
        validate_limit(1000)

    def test_invalid_type(self):
        """Should reject non-integers."""
        with pytest.raises(ValidationError, match="should be an integer"):
            validate_limit("25") # type: ignore

    def test_limit_too_high(self):
        """Should reject limits over 1000."""
        with pytest.raises(ValidationError, match="between 0 and 1000"):
            validate_limit(1001)

    def test_negative_limit(self):
        """Should reject negative limits."""
        with pytest.raises(ValidationError, match="between 0 and 1000"):
            validate_limit(-1)


class TestValidateOffset:
    """Tests for validate_offset."""

    def test_valid_offset(self):
        """Should accept valid offsets."""
        validate_offset(0)
        validate_offset(100)

    def test_invalid_type(self):
        """Should reject non-integers."""
        with pytest.raises(ValidationError, match="should be an integer"):
            validate_offset("0") # type: ignore


class TestValidateSortField:
    """Tests for validate_sort_field."""

    def test_valid_fields(self):
        """Should accept valid sort fields."""
        validate_sort_field(None)
        validate_sort_field("id")
        validate_sort_field("name")
        validate_sort_field("mindate")
        validate_sort_field("maxdate")
        validate_sort_field("datacoverage")

    def test_invalid_field(self):
        """Should reject invalid sort fields."""
        with pytest.raises(ValidationError, match="must be one of"):
            validate_sort_field("invalid")

    def test_invalid_type(self):
        """Should reject non-strings."""
        with pytest.raises(ValidationError, match="should be a string"):
            validate_sort_field(123) # type: ignore


class TestValidateSortOrder:
    """Tests for validate_sort_order."""

    def test_valid_orders(self):
        """Should accept valid sort orders."""
        validate_sort_order("asc")
        validate_sort_order("desc")

    def test_invalid_order(self):
        """Should reject invalid sort orders."""
        with pytest.raises(ValidationError, match="must be one of"):
            validate_sort_order("ascending")

    def test_invalid_type(self):
        """Should reject non-strings."""
        with pytest.raises(ValidationError, match="should be a string"):
            validate_sort_order(123) # type: ignore


class TestValidateUnits:
    """Tests for validate_units."""

    def test_valid_units(self):
        """Should accept valid units."""
        validate_units("metric")
        validate_units("standard")

    def test_invalid_units(self):
        """Should reject invalid units."""
        with pytest.raises(ValidationError, match="must be one of"):
            validate_units("imperial")

    def test_invalid_type(self):
        """Should reject non-strings."""
        with pytest.raises(ValidationError, match="should be a string"):
            validate_units(123) # type: ignore


class TestValidateBoolean:
    """Tests for validate_boolean."""

    def test_valid_boolean(self):
        """Should accept booleans."""
        validate_boolean(True, "param")
        validate_boolean(False, "param")

    def test_invalid_int(self):
        """Should reject integers (even 0 and 1)."""
        with pytest.raises(ValidationError, match="should be a boolean"):
            validate_boolean(1, "param")

    def test_invalid_string(self):
        """Should reject strings."""
        with pytest.raises(ValidationError, match="should be a boolean"):
            validate_boolean("true", "param")
