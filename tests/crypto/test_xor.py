from ctflib import xor


def test_xor_single():
    assert xor(b'something', 1) == b'rnlduihof'


def test_xor_cycle():
    assert xor(b'something', b'\x01\x02\x03', cycle_key=True) == b'rmndvkhld'


def test_xor_no_cycle():
    assert xor(b'something', b'\x01\x02\x03', cycle_key=False) == b'rmnething'
