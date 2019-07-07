# -*- coding: utf-8 -*-
"""setuptools control."""

import re

from setuptools import setup


def get_version():
    """Return __version__ value from main source file."""
    with open("aviasales/__init__.py") as source:
        version = re.search(r"^__version__\s*=\s*'(.*)'",
                            source.read(),
                            re.M).group(1)
    return version


def get_description():
    """Return long description from README."""
    with open("README.rst", "rb") as readme:
        long_description = readme.read().decode("utf-8")
    return long_description


setup(
    name="aviasales",
    packages=["aviasales"],
    package_data={'aviasales': ['*.xml']},
    test_suite="tests",
    entry_points={
        "console_scripts": [
            "aviasales = aviasales.__main__:main"
        ]
    },
    version=get_version(),
    description="Web service that provides flights API.",
    long_description=get_description(),
    long_description_content_type="text/x-rst",
    author="Egor Artemov",
    author_email="egor.artemov@gmail.com",
    license="WTFPL",
    url="https://github.com/souryogurt/aviasales",
    install_requires=["aiohttp"],
    setup_requires=[]
)
