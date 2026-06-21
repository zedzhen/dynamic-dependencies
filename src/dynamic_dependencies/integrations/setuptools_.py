__all__ = ["finalize_distribution_options"]

from setuptools import Distribution

from dynamic_dependencies import dependencies, optional_dependencies, Config


def finalize_distribution_options(dist: Distribution) -> None:
    config = Config.from_pyproject()
    if config.require is not None:
        dist.install_requires = dependencies(config)
    if config.optional is not None:
        dist.extras_require = optional_dependencies(config)
