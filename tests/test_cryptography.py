from cryptography import __version__
from cryptography.crpytography import *

def test_version():
    assert __version__ == '0.1.0'



def test_encrypt_string_with_given_shift():
    actual = encrypt('abc',1)
    expected = 'bcd'
    assert actual == expected


# decrypt a previously encrypted string with the same shift
def test_decrypt_encrypted_text():
    actual = decrypt('bcd',1)
    expected = 'abc'
    assert actual == expected
