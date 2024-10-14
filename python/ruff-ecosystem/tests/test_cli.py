"""Test cli."""

import pytest

from ruff_ecosystem.cli import excepthook


@pytest.mark.skip(reason="needs implementation")
@pytest.mark.parametrize(
    "interactive, isatty, call_default",
    [
        (True, False, True),
        (False, False, True),
        (False, True, False),
    ],
)
def test_excepthook(interactive, isatty, call_default, mocker):
    """Test excepthook behavior based on interactive mode and tty presence."""
    mock_type = mocker.Mock()
    mock_value = mocker.Mock()
    mock_tb = mocker.Mock()

    mocker.patch("sys.ps1", new_callable=mocker.PropertyMock, return_value=interactive)
    mocker.patch("sys.stderr.isatty", return_value=isatty)
    default_hook = mocker.patch("sys.__excepthook__")
    print_exc = mocker.patch("traceback.print_exception")
    pdb_post_mortem = mocker.patch("pdb.post_mortem")

    excepthook(mock_type, mock_value, mock_tb)

    if call_default:
        default_hook.assert_called_once_with(mock_type, mock_value, mock_tb)
        print_exc.assert_not_called()
        pdb_post_mortem.assert_not_called()
    else:
        default_hook.assert_not_called()
        print_exc.assert_called_once_with(mock_type, mock_value, mock_tb)
        pdb_post_mortem.assert_called_once_with(mock_tb)
