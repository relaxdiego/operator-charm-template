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


_NAME = 'changeme'
setup(
    name=_NAME,
    version='0.1.0',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.8',
    ],
    author='changeme',
    author_email='changeme@changeme.com',
    include_package_data=True,
    install_requires=[
        'ops>=0.7.0,<0.8.0',
    ]
)
