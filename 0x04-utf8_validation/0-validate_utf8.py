#!/usr/bin/python3
"""
Check data set represents a valid UTF-8 encoding
"""

def validUTF8(data):
    num_bytes_to_follow = 0

    for byte in data:
        byte = byte & 255  # Ensure only the least significant 8 bits are considered
        if num_bytes_to_follow == 0:
            if byte >> 7 == 0b0:
                num_bytes_to_follow = 0
            elif byte >> 5 == 0b110:
                num_bytes_to_follow = 1
            elif byte >> 4 == 0b1110:
                num_bytes_to_follow = 2
            elif byte >> 3 == 0b11110:
                num_bytes_to_follow = 3
            else:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            num_bytes_to_follow -= 1

    return num_bytes_to_follow == 0

# Test cases
data = [65]
print(validUTF8(data))  # Output: True

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))  # Output: True

data = [229, 65, 127, 256]
print(validUTF8(data))  # Output: False
