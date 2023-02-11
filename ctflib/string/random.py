"""Generate random strings for different purposes."""

from secrets import choice
from typing import Sequence

from .consts import alphanumeric


def random_string(length: int = 32, alphabet: Sequence[str] = alphanumeric) -> str:
    """
    Generate random string from characters.

    Args
    ----
        length (int, optional): Length of random string. Defaults to 32.
        alphabet (Sequence[str], optional): Characters to choose from.
            Defaults to alphanumeric.

    Returns
    -------
        str: randomly generated string
    """
    return ''.join(choice(alphabet) for _ in range(length))
