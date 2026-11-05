from importlib.metadata import version

import scopepilot


def test_scopepilot_is_importable() -> None:
    assert scopepilot.__file__ is not None


def test_scopepilot_package_version() -> None:
    assert version("scopepilot") == "0.1.0.dev0"
