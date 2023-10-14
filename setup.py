"""Setup for consulta-cep.
"""

import os

from setuptools import find_packages, setup


def read(*paths):
    """Read the contents of a text file safely.
    >>> read("project_name", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """
    root_path = os.path.dirname(__file__)
    filepath = os.path.join(root_path, *paths)
    with open(filepath) as file_:
        return file_.read().strip()


def read_requirements(path):
    """Return a list of requirements from a text file"""
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(("#", "git+", '"', "-"))
    ]


setup(
    name="consulta-cep",
    version="0.1.0",
    description="Consulta CEP",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Carlos Moreno",
    author_email=[
        "omorenodovale@gmail.com",
    ],
    python_requires=">=3.9",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    entry_points={"console_scripts": {"consulta-cep = app.__main__:main"}},
    install_requires=read_requirements("requirements.txt"),
    extras_require={
        "test": read_requirements("requirements.test.txt"),
        "dev": read_requirements("requirements.dev.txt"),
    },
)
