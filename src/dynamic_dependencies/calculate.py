__all__ = ["dependencies", "optional_dependencies"]

from dynamic_dependencies.config import Config


def dependencies(config: Config) -> list[str] | None:
    if config.require is None:
        return None
    return config.resolve(config.require)


def optional_dependencies(config: Config) -> dict[str, list[str]] | None:
    if config.optional is None:
        return None
    return {key: config.resolve(value) for key, value in config.optional.items()}
