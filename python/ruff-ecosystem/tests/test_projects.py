"""Projects tests."""

from ruff_ecosystem.projects import (
    CheckOptions,
    ConfigOverrides,
    FormatOptions,
    Project,
    Repository,
)


def test_project():
    """Test project."""
    expected = Project(
        repo=Repository(owner="testowner", name="testname", ref="testref"),
        check_options=CheckOptions(
            preview=False,
            select="",
            ignore="",
            exclude="",
            show_fixes=False,
            max_lines_per_rule=50,
        ),
        format_options=FormatOptions(preview=False, exclude=""),
        config_overrides=ConfigOverrides(
            always={}, when_preview={}, when_no_preview={}
        ),
    )

    result = Project(repo=Repository(owner="testowner", name="testname", ref="testref"))

    assert result == expected
