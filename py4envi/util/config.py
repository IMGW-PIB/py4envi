import os
from configparser import ConfigParser
from pathlib import Path


class CaseConfigParser(ConfigParser):
    """Avoid infinite loop when using uppercase configs from Env.
    Explanation: The problem here is with optionxform, which turns all options to lower case by default.
    Eventually, it will have key and value equal.
    """

    def optionxform(self, optionstr):
        return optionstr


def current_file_folder() -> Path:
    return Path(__file__).absolute().resolve().parent


def read(*filenames) -> CaseConfigParser:
    """Reads the specified file as config

    Arguments:
        filenames -- files to read

    Returns:
        configparser.ConfigParser -- parsed config
    """

    config = CaseConfigParser(os.environ)
    config.read(filenames)
    return config


def get_section(section: str):
    """Gets a speficied section from the config file

    Arguments:
        section {str} -- section to get from the file

    Returns:
        Section from the config file
    """
    return read("sats.ini", str(current_file_folder().joinpath('sats.ini')), str(
        current_file_folder().parent.joinpath('sats.ini')), "overrides.ini")[section]


class Sat4enviConfig:
    _section = get_section('sat4envi')

    @property
    def url(self) -> str:
        """
        full api url (with version)
        """
        return self._section['url']

    @property
    def token_cache_filename(self) -> str:
        """
        name of the file to cache the daily token
        """
        return self._section['token_cache_filename']


class RestConfig:
    _section = get_section('rest')

    @property
    def timeout(self) -> int:
        """
        connection timeout in seconds
        """
        return int(self._section['timeout'])

    @property
    def max_retries(self) -> int:
        """
        max connection retries
        """
        return int(self._section['max_retries'])

    @property
    def backoff_factor(self) -> int:
        """
        backoff factor applied after each failed connection attempt
        """
        return int(self._section['backoff_factor'])
