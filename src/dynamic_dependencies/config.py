__all__ = ["Config"]

import sys
from dataclasses import dataclass
from functools import cached_property
from os import PathLike

from dependency_groups import DependencyGroupResolver
from typing_extensions import Self

if sys.version_info >= (3, 11):
    import tomllib
else:
    import tomli as tomllib


@dataclass
class Config:
    dependency_groups: dict[str, list[str | dict[str, str]]]
    require: str | None = None
    optional: dict[str, str] | None = None

    @classmethod
    def from_pyproject(cls, file: str | PathLike[str] = "pyproject.toml") -> Self:
        with open(file, "rb") as f:
            data = tomllib.load(f)
        tool_data = data.get("tool", {}).get("dynamic_dependencies", {})
        dependency_groups = data.get("dependency-groups", {})
        return cls(dependency_groups=dependency_groups, **tool_data)

    @cached_property
    def resolver(self) -> DependencyGroupResolver:
        return DependencyGroupResolver(self.dependency_groups)

    def resolve(self, group: str) -> list[str]:
        return list(map(str, self.resolver.resolve(group)))
