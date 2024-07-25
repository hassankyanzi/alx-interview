def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    """
    num_bytes = 0

    for num in data:
        # Check if the number is in the valid byte range
        if num < 0 or num > 255:
            return False
        
        # Determine the number of bytes in the current character
        if num_bytes == 0:
            if (num >> 7) == 0b0:
                # 1-byte character
                continue
            elif (num >> 5) == 0b110:
                # 2-byte character
                num_bytes = 1
            elif (num >> 4) == 0b1110:
                # 3-byte character
                num_bytes = 2
            elif (num >> 3) == 0b11110:
                # 4-byte character
                num_bytes = 3
            else:
                return False
        else:
            if (num >> 6) != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0
