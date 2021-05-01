import pathlib
from setuptools import setup, find_packages
from py4envi import __version__

NAME = "py4envi"
REQUIRES = [
    "urllib3 >= 1.25.3",
    "requests >= 2.25.1",
    "python-dateutil >= 2.8.1",
    "Shapely >= 1.7.1",
    "geopandas >= 0.9.0",
    "tqdm >= 4.60.0",
]

HERE = pathlib.Path(__file__).parent
# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name=NAME,
    version=__version__,
    author="Konrad Malik",
    author_email="konrad.malik@gmail.com",
    license="LGPL-2.1",
    description="Library/cli tool for https://dane.sat4envi.imgw.pl/",
    url="https://github.com/IMGW-PIB/py4envi",
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description=README,
    long_description_content_type="text/markdown",
    entry_points={
        "console_scripts": ["py4envi = py4envi.__main__:main"],
    },
    classifiers=[
        "License :: OSI Approved :: LGPL-2.1 License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
