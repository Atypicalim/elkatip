# encoding=utf-8

from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name = "elkatip",
    version = "0.1.3",
    keywords = ("uyghur", "uighur","alkatip", "elkatip", "base", "ext", "convert", "tool", "gui"),
    description = "Uighur string convert tool for gui",
    long_description = long_description,
    long_description_content_type="text/markdown",
    license = "MIT Licence",

    url = "https://github.com/kompasim/elkatip",
    author = "kompasim",
    author_email = "kompasim@163.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = [],
    classifiers= [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
