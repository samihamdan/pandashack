import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pandashack',
    version='0.0.1',
    author='Sami Hamdan',
    author_email='sami.hamdan@hhu.de',
    description='A small library extending pandas method chaining api',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/samihamdan/pandashack",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
