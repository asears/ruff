"""Test format."""

from ruff_ecosystem.format import markdown_format_result


def test_markdown_format_result(mocker):
    """Test markdown format result."""
    result = mocker.MagicMock()
    result = markdown_format_result(result=result)
