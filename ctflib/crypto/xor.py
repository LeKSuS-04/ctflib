"""Contains `xor` function."""

from itertools import cycle, zip_longest
from typing import Iterable


def xor(data: Iterable[int], key: Iterable[int] | int, cycle_key: bool = True) -> bytes:
    """
    Xor two integer sequences.

    Args:
        data (Iterable[int]): data to be xored
        key (Iterable[int] | int): key to xor with
        cycle_key (bool, optional): cycle through the key. Defaults to True.

    Returns
    -------
        bytes: result of xoring data with key
    """
    if isinstance(key, int):
        key = [key]

    if cycle_key:
        values = zip(data, cycle(key), strict=False)
    else:
        values = zip_longest(data, key, fillvalue=0)
    return bytes(a ^ b for a, b in values)
