"""Test main."""

from enum import Enum

import pytest

from ruff_ecosystem.main import OutputFormat


class OutputFormat(Enum):
    markdown = "markdown"
    json = "json"


@pytest.mark.parametrize(
    "format_name, expected_value",
    [
        ("markdown", "markdown"),
        ("json", "json"),
    ],
)
def test_output_format_enum(format_name, expected_value):
    """Test that OutputFormat enum contains correct values."""
    assert getattr(OutputFormat, format_name).value == expected_value
