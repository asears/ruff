"""Test check."""

import ruff_ecosystem.check as check


def test_check():
    """Check constants exist."""
    assert check.CHECK_SUMMARY_LINE_RE is not None
    assert check.CHECK_DIFF_LINE_RE is not None
    assert check.CHECK_DIAGNOSTIC_LINE_RE is not None
    assert check.CHECK_VIOLATION_FIX_INDICATOR is not None
    assert check.GITHUB_MAX_COMMENT_LENGTH is not None
