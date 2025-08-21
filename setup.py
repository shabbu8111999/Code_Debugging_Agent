from setuptools import setup, find_packages

setup(
    name="code_debugging_agent",
    version="0.1.0",
    author="Shabareesh Nair",
    author_email="shabareesh12@gmail.com",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "debug-agent=main:run",  # CLI entry
        ],
    },
)
