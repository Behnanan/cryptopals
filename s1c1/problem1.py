#!/usr/bin/env python
# Convert hex to base64

hex = b'49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
base64 = b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

import binascii
import base64

def hex_to_bytes(data):
    byte = binascii.unhexlify(data)
    return byte

def bytes_to_base64(data):
    byte = base64.b64encode(data)
    return byte

raw = hex_to_bytes(hex)
conversion = bytes_to_base64(raw)
print(conversion)