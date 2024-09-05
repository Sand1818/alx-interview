#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    Dertermnes if data reptesents a valid UTF-8 encoding
    """
    def cont_byte(byte):
        return (byte & 0xC0) == 0x80

    num_o_bytes = 0

    for byte in data:
        if num_o_bytes == 0:
            if (byte & 0x80) == 0x00:
                continue
            elif (byte & 0xE0) == 0xC0:
                num_o_bytes = 1
            elif (byte & 0xF0) == 0xE0:
                num_o_bytes = 2
            elif (byte & 0xF8) == 0xF0:
                num_o_bytes = 3
            else:
                return False
        else:
            if not cont_byte(byte):
                return False
            num_o_bytes -= 1

    return num_o_bytes == 0
