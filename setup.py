import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    # TODO: change package name
    name="example-pkg-mpenhallegon", # Replace with your own username
    version="0.0.1",
    # TODO: change name and email
    author="Micahel Penhallegon",
    author_email="michael.penhallegon@bms.com",
    # TODO: add a descriptive summary
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # TODO: change link to repo and bug_tracker
    url="https://github.com/mpenhall-celgene/pytemplate",
    project_urls={
        "Bug Tracker": "https://github.com/mpenhall-celgene/pytemplate/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)