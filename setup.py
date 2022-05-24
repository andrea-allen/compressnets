from setuptools import find_packages
import setuptools

VERSION = '0.0.2'
DESCRIPTION = 'CompressNets package for temporal network and contact data compression'
LONG_DESCRIPTION = 'CompressNets is a Python package that supports compression of user-specified adjacency matrices ' \
                   'encoding temporal contact data. Using an original compression algorithm, a simplified compressed ' \
                   'version of the contact data is generated, to lower resolution of the data while maintaining ' \
                   'important temporal structural features.'

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="compressnets",
    version=VERSION,
    author="Andrea Allen",
    author_email="andrea2allen@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],  # add any additional packages that
    # needs to be installed along with your package.

    keywords=['python', 'compressnets'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires=">=3.6",
)