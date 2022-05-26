from setuptools import find_packages
import setuptools

VERSION = '0.1.6'
DESCRIPTION = 'CompressNets package for temporal network and contact data compression'

with open("README.md", "r", encoding="utf-8") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name="compressnets",
    version=VERSION,
    author="Andrea Allen",
    author_email="andrea2allen@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],  # add any additional packages that
    # needs to be installed along with your package.

    keywords=['python', 'compressnets'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires=">=3.6",
    include_package_data=True,
)

## helpful article: https://py-pkgs.org/04-package-structure

# [build-system]
# requires = [
#     "setuptools>=61.0.0",
#     "wheel"
# ]
# build-backend = "setuptools.build_meta"
