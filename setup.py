from setuptools import find_packages, setup

from colorbox import __author__, __name__, __version__

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name=__name__,
    version=__version__,
    author=__author__,
    description="Color box that provides various colors‘ rgb decimal code.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zhangxianbing/colorbox",
    packages=find_packages(include=[f"{__name__}*"]),
    python_requires=">=3.6",
    license="Apache License 2.0",
    keywords="options, argparse, config, cli, YAML, INI",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
)
