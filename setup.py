#
# This file is not necessary for building charms but is, instead, just meant to make
# unit testing easier. By maintaining this file and running `make dependencies`, your
# unit tests will now only need to `from src.charm import ChangeMeCharm` without
# needing to remember to add `sys.path.append('src')` at the top of each test file.
#
from sys import version_info

from setuptools import find_packages, setup

minimum_python_version = (3, 5, 0)

if version_info[:3] < minimum_python_version:
    raise RuntimeError(
        'Unsupported python version {}. Please use {} or newer'.format(
            '.'.join(map(str, version_info[:3])),
            '.'.join(map(str, minimum_python_version)),
        )
    )


setup(
    name='changeme',
    version='0.1.0',
    packages=find_packages(),
    # Always place your charm's dependencies here and not directly in requirements.txt.
    # This ensures that when `make dependencies` runs, it will install the runtime
    # dependencies correctly. In addition, `make dependencies` will take care of
    # updating and pinning the runtime dependencies in requirements.txt so that you
    # don't have to. For more info, please see "Adding A Runtime Dependency" in this
    # project's README.md file
    install_requires=[
        'ops>=0.7.0,<0.8.0',
    ]
)
