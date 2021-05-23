import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    # TODO: change package name
    name="pystandlogger", # Replace with your own username
    version="0.0.1",
    # TODO: change name and email
    author="Micahel Penhallegon",
    author_email="mike@hematite.tech",
    # TODO: add a descriptive summary
    description="an example of utilizing logger in ECS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # TODO: change link to repo and bug_tracker
    url="https://github.com/mpenhall-celgene/pyloggerkinesis",
    project_urls={
        "Bug Tracker": "https://github.com/mpenhall-celgene/pyloggerkinesis/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    install_requires=["numpy"],
    python_requires='>=3.6',
)