import statistics
from collections import Counter
from math import sqrt

import pytest

from ctflib import random_string

alphanumeric = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'


def generate_sample(
    size: int, length: int | None = None, alphabet: str | None = None
) -> list[str]:
    kwargs = {'length': length, 'alphabet': alphabet}
    to_remove = []
    for k, v in kwargs.items():
        if v is None:
            to_remove.append(k)
    for k in to_remove:
        kwargs.pop(k)

    return [random_string(**kwargs) for _ in range(size)]


@pytest.fixture
def sample():
    return generate_sample(20_000, 32, alphanumeric)


def consists_of(string: str, characters: str) -> bool:
    return all(c in characters for c in string)


def test_basic():
    length = 32
    alphabet = 'abc'
    result = random_string(length, alphabet)
    assert len(result) == length
    assert consists_of(result, alphabet)


def test_large_sample(sample: list[str]):
    assert all(len(string) == 32 for string in sample)
    assert all(consists_of(string, alphanumeric) for string in sample)


def test_uniqueness(sample: list[str]):
    unique = set(sample)
    assert len(sample) == len(unique)


def test_distribution():
    """Checks randomness of distribution by checking 3-sigma rule."""
    sample_size, string_length, alphabet = 100, 32, alphanumeric

    repeat_times = 100
    failure_count = 0
    alphabet_size = len(alphabet)
    total_chars = sample_size * string_length
    for _ in range(repeat_times):
        all_generated = ''.join(generate_sample(sample_size, string_length, alphabet))
        distribution = Counter(all_generated)

        expectation = total_chars / alphabet_size
        variance = statistics.variance(distribution.values())
        std = sqrt(variance)

        for character_count in distribution.values():
            if abs(character_count - expectation) > 3 * std:
                failure_count += 1

    success_rate = 1 - failure_count / (repeat_times * alphabet_size)
    assert success_rate > 0.995
