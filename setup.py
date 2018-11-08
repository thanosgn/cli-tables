import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cli_tables",
    version="0.0.2",
    author="Thanos Giannooulos",
    author_email="thanosgn@gmail.com",
    description="Create pretty looking ascii tables",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thanosgn/cli-tables",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
