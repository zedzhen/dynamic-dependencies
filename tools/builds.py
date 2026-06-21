import sys
from os import PathLike, getcwd
from pathlib import Path

from build import ProjectBuilder
from build.env import DefaultIsolatedEnv
from typing_extensions import Any

if sys.version_info >= (3, 11):
    from contextlib import chdir
else:
    from os import chdir as os_chdir

    class chdir:
        _path: str | bytes | PathLike[Any]
        _old: list[str]

        def __init__(self, path: str | bytes | PathLike[Any]) -> None:
            self._path = path
            self._old = []

        def __enter__(self) -> None:
            self._old.append(getcwd())
            os_chdir(self._path)

        def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
            os_chdir(self._old.pop())


base_dir = Path(__file__).resolve().parent.parent

out = "dist/"

out_compat: str | PathLike[str]
if "--one-out" in sys.argv:
    out_compat = Path("dist/").resolve()
else:
    out_compat = "dist/"

with chdir(base_dir):
    with DefaultIsolatedEnv() as env:
        builder = ProjectBuilder(".", env.python_executable)
        env.install(builder.build_system_requires)

        builder.build("sdist", out)
        wheel_file = builder.build("wheel", out)

    with chdir("compat/setuptools"), DefaultIsolatedEnv() as env:
        builder = ProjectBuilder(".", env.python_executable)
        env.install([wheel_file])
        env.install(builder.build_system_requires)

        builder.build("sdist", out_compat)
        builder.build("wheel", out_compat)
