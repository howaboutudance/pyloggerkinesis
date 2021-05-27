import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pystandlogger",
    version="0.1.0",
    author="Micahel Penhallegon",
    author_email="mike@hematite.tech",
    description="an example of utilizing logger in ECS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mpenhall-celgene/pyloggerkinesis",
    project_urls={
        "Bug Tracker": "https://github.com/mpenhall-celgene/pyloggerkinesis/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    install_requires=[
        "numpy",
        "aws-logging-handlers"
        ],
    python_requires='>=3.6',
)