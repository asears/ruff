"""Test defaults."""

import ruff_ecosystem.defaults as default


def test_defaults():
    """Test defaults"""
    assert default.JUPYTER_NOTEBOOK_SELECT
    assert default.DEFAULT_TARGETS
