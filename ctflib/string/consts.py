"""More string constants in addition to `string` module."""

from string import ascii_letters, digits

alphanumeric = ascii_letters + digits
base64alpha = alphanumeric + '+/='
