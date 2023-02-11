from ctflib import alphanumeric, base64alpha


def should_contain(value: str, characters: str):
    assert all(c in value for c in characters)


def test_alphanumeric():
    should_contain(
        alphanumeric, 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    )


def test_base64lpha():
    should_contain(
        base64alpha, 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/='
    )
