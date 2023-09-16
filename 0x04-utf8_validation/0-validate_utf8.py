#!/usr/bin/python3
""" Data set represents a valid UTF-8 encoding. """


def validUTF8(data):
    """
    Check data set represents a valid UTF-8 encoding.

    Return: `True` if data is a valid UTF-8 encoding, else return `False`

    A character in UTF-8 can be 1 to 4 bytes long.

    The data set can contain multiple characters.

    The data will be represented by a list of integers.

    Each integer represents 1 byte of data, therefore you only
    need to handle the 8 least significant bits of each integer.
    
    """
    # Initialize a variable to keep track of the number of 
    # expected continuation bytes
    num_continuation_bytes = 0

    # Iterate through each integer in the data list
    for num in data:
        # Convert the integer to its binary representation with 
        # 8 least significant bits
        binary_repr = format(num, '08b')

        # If we're not expecting any continuation bytes, this should start with '0'
        if num_continuation_bytes == 0:
            if binary_repr[0] == '0':
                continue  # Single-byte character, move to the next integer
            elif binary_repr.startswith('110'):
                num_continuation_bytes = 1  # Expecting 1 continuation byte
            elif binary_repr.startswith('1110'):
                num_continuation_bytes = 2  # Expecting 2 continuation bytes
            elif binary_repr.startswith('11110'):
                num_continuation_bytes = 3  # Expecting 3 continuation bytes
            else:
                return False  # Invalid leading bits

        # If we're expecting continuation bytes, the integer should start with '10'
        else:
            if not binary_repr.startswith('10'):
                return False  # Invalid continuation byte
            num_continuation_bytes -= 1

    # After processing all integers, num_continuation_bytes should be 0
    return num_continuation_bytes == 0
