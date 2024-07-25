def validUTF8(data):
    """
    Check if the data set represents a valid UTF-8 encoding.
    
    :param data: List of integers representing the bytes of the data set
    :return: True if data is a valid UTF-8 encoding, else False
    """
    num_bytes = 0

    # Masks to check the most significant bits of a byte
    mask1 = 1 << 7    # 10000000
    mask2 = 1 << 6    # 01000000

    for num in data:
        if num < 0 or num > 255:
            return False

        mask = 1 << 7
        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            while mask & num:
                num_bytes += 1
                mask >>= 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check that the remaining bytes start with 10
            if not (num & mask1 and not (num & mask2)):
                return False

        num_bytes -= 1

    return num_bytes == 0

if __name__ == "__main__":
    # Example data
    data1 = [65]
    print(validUTF8(data1))  # Expected Output: True

    data2 = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data2))  # Expected Output: True

    data3 = [229, 65, 127, 256]
    print(validUTF8(data3))  # Expected Output: False
