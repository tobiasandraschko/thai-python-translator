from setuptools import setup, find_packages

setup(
    name="thai-python-translator",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "thai-python=translator.cli:main",
        ],
    },
)