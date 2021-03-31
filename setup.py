from setuptools import setup, find_packages
from py4envi import __version__

NAME = "py4envi"
REQUIRES = [
    "urllib3 >= 1.25.3",
    "python-dateutil",
    "Shapely >= 1.7.1",
]

setup(
    name=NAME,
    version=__version__,
    author='Konrad Malik',
    author_email='konrad.malik@imgw.pl',
    description="Library/cli tool for https://dane.sat4envi.imgw.pl/",
    url="https://dane.sat4envi.imgw.pl/",
    keywords=["sat4envi", "api", "sentinel", "esa", "imgw"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
        Library/cli tool for https://dane.sat4envi.imgw.pl/
    """
)
