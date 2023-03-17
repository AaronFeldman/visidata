# SPDX-License-Identifier: MIT

from setuptools import setup, find_packages
from pathlib import Path


exec(Path('__about__.py').read_text())


def readme():
    return Path("README.md").read_text()


def requirements():
    return Path("requirements.txt").read_text().splitlines()


setup(
        name="vdsql",
        version=__version__,
        description=__description__,
        long_description=readme(),
        long_description_content_type="text/markdown",
        classifiers=[
            "Development Status :: 4 - Beta",
            "Programming Language :: Python :: 3",
        ],
        keywords="visidata sql rdbms ibis substrait",
        author="Saul Pwanson",
        url="https://github.com/visidata/vdsql",
        python_requires=">=3.8",
        packages=find_packages(exclude=["tests"]),
        entry_points={'visidata.plugins': 'vdsql=visidata.apps.vdsql',
            'console_scripts': ['vdsql =visidata.apps.vdsql.__main__:main']},
        install_requires=requirements(),
)
