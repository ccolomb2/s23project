"""
This is a Python package for printing references.
"""

from setuptools import setup

setup(
    name="pkg",
    version="0.0.1",
    description="s23project package",
    maintainer="<Carolina Colombo Tedesco>",
    maintainer_email="<ccolomb2@andrew.cmu.edu>",
    license="MIT",
    packages=["pkg"],
    entry_points={
        "console_scripts": ["commandline = s23project.terminal_command:terminal"]
    },
    long_description="""bibtex or ris format""",
)
