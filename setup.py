import os
import sys

from setuptools import Distribution, setup

sys.path.insert(0, os.path.abspath("src"))
from dynamic_dependencies.integrations.setuptools_ import finalize_distribution_options

_finalize_options = Distribution.finalize_options


def finalize_options(self: Distribution):
    _finalize_options(self)
    finalize_distribution_options(self)
    if not isinstance(self.extras_require, dict):
        self.extras_require = {}
    self.extras_require["setuptools"] = [f"dynamic_dependencies_setuptools=={self.metadata.version}"]


Distribution.finalize_options = finalize_options

setup()
