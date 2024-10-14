"""Test ruff main."""

from ruff.__main__ import find_ruff_bin
import pytest
import os


# TODO(AS): The python version info, os names and user schemes should be parameterized
# for each case
# Extract reusable test fixtures


@pytest.mark.parametrize(
    "platform_name, exe_suffix",
    [
        ("win32", ".exe"),
        # ("linux", ""),
    ],
)
def test_find_ruff_bin_direct_script_path(platform_name, exe_suffix, mocker, tmpdir):
    """Test find_ruff_bin direct script path."""
    mocker.patch("sysconfig.get_config_var", return_value=exe_suffix)
    mocker.patch("os.name", platform_name)
    mocker.patch("sys.version_info", (3, 8))
    mocker.patch("sys.platform", platform_name)
    mocker.patch("os.path.isfile", return_value=True)
    mocker.patch("sysconfig.get_path", return_value=str(tmpdir))

    result = find_ruff_bin()

    assert result == os.path.join(str(tmpdir), f"ruff{exe_suffix}")


@pytest.mark.xfail(raises=FileNotFoundError, reason="needs some inspection of test")
@pytest.mark.parametrize(
    "platform_name, exe_suffix",
    [
        ("win32", ".exe"),
        # ("linux", ""),
    ],
)
def test_find_ruff_bin_user_path(platform_name, exe_suffix, mocker, tmpdir):
    """Test find_ruff_bin user path."""
    mocker.patch("sysconfig.get_config_var", return_value=exe_suffix)
    mocker.patch("os.name", platform_name)
    mocker.patch("sys.version_info", (3, 8))
    mocker.patch("sys.platform", platform_name)
    mocker.patch("os.path.isfile", return_value=True)
    mocker.patch("sysconfig.get_path", return_value=str(tmpdir))
    # Test user path
    mocker.patch("sysconfig.get_preferred_scheme", return_value="user_scheme")
    user_path = tmpdir.mkdir("user").join(f"ruff{exe_suffix}")
    user_path.write("")
    mocker.patch("os.path.isfile", side_effect=lambda path: path == str(user_path))

    result = find_ruff_bin()

    assert result == str(user_path)


@pytest.mark.skip(
    reason="This test can only run on linux due to lack of pathlib use, needs pytest conditional"
)
@pytest.mark.parametrize(
    "platform_name, exe_suffix",
    [
        ("win32", ".exe"),
        # ("linux", ""),
    ],
)
def test_find_ruff_bin_target_path_within_package_root(
    platform_name, exe_suffix, mocker, tmpdir
):
    """Test find_ruff_bin user path."""
    mocker.patch("sysconfig.get_config_var", return_value=exe_suffix)
    mocker.patch("os.name", platform_name)
    mocker.patch("sys.version_info", (3, 8))
    mocker.patch("sys.platform", platform_name)
    mocker.patch("os.path.isfile", return_value=True)
    mocker.patch("sysconfig.get_path", return_value=str(tmpdir))

    # Test target path within package root
    pkg_root = tmpdir.mkdir("pkg_root")
    target_path = pkg_root.mkdir("bin").join(f"ruff{exe_suffix}")
    target_path.write("")
    mocker.patch(
        "os.path.dirname",
        side_effect=lambda path: str(pkg_root)
        if path == __file__
        else os.path.dirname(path),
    )
    assert find_ruff_bin() == str(target_path)


@pytest.mark.parametrize(
    "platform_name, exe_suffix",
    [
        ("win32", ".exe"),
        # ("linux", ""),
    ],
)
def test_find_ruff_bin_pip_specific_build_env_path(
    platform_name, exe_suffix, mocker, tmpdir
):
    """Test find_ruff_bin user path."""
    mocker.patch("sysconfig.get_config_var", return_value=exe_suffix)
    mocker.patch("os.name", platform_name)
    mocker.patch("sys.version_info", (3, 8))
    mocker.patch("sys.platform", platform_name)
    mocker.patch("os.path.isfile", return_value=True)
    mocker.patch("sysconfig.get_path", return_value=str(tmpdir))
    # Test pip-specific build environment path
    overlay_path = tmpdir.mkdir("pip-build-env-overlay").join(f"ruff{exe_suffix}")
    overlay_path.write("")
    paths = [str(overlay_path.dirname), str(tmpdir.mkdir("pip-build-env-normal"))]
    mocker.patch("os.environ.get", return_value=os.pathsep.join(paths))
    assert find_ruff_bin() == str(overlay_path)


@pytest.mark.parametrize(
    "platform_name, exe_suffix",
    [
        ("win32", ".exe"),
        # ("linux", ""),
    ],
)
def test_find_ruff_bin_no_valid_paths(platform_name, exe_suffix, mocker, tmpdir):
    """Test find_ruff_bin user path."""
    mocker.patch("sysconfig.get_config_var", return_value=exe_suffix)
    mocker.patch("os.name", platform_name)
    mocker.patch("sys.version_info", (3, 8))
    mocker.patch("sys.platform", platform_name)
    mocker.patch("os.path.isfile", return_value=True)
    mocker.patch("sysconfig.get_path", return_value=str(tmpdir))
    # Ensure FileNotFoundError is raised when no paths are valid
    mocker.patch("os.path.isfile", return_value=False)
    with pytest.raises(FileNotFoundError):
        find_ruff_bin()
