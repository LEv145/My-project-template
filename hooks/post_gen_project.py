from __future__ import annotations

import typing as t
import shutil
from pathlib import Path


PROJECT_DIRECTORY = Path(".").absolute()


def remove(filepath: str) -> None:
    target = PROJECT_DIRECTORY / filepath

    if target.is_dir():
        shutil.rmtree(target, ignore_errors=True)
    else:
        target.unlink()


def main() -> None:
    if "{{cookiecutter.open_source_license}}" == "Not open source":
        remove("LICENSE")


if __name__ == "__main__":
    main()
