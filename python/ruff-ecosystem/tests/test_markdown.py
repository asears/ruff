"""Markdown tests."""

from ruff_ecosystem.markdown import markdown_project_section


def test_markdown_project_section(mocker):
    """Test markdown project section."""
    title = "abc"
    content = "123"
    options = mocker.MagicMock()
    project = mocker.MagicMock()
    expected = "details"

    result = str(
        markdown_project_section(
            title=title, content=content, options=options, project=project
        )
    )

    assert expected in result
