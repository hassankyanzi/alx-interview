# Create the README.md file with the provided content
readme_content = """
# 0x04. UTF-8 Validation

## Description

This project involves validating whether a given dataset represents a valid UTF-8 encoding using Python. You will need to apply your knowledge of bitwise operations, the UTF-8 encoding scheme, and Python programming skills to determine the validity of UTF-8 encoded data.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3)
- All files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- Your code should use the PEP 8 style (version 1.7.x)
- All your files must be executable

## Concepts

- **Bitwise Operations in Python**: Understanding how to manipulate bits in Python, including operations like AND (&), OR (|), XOR (^), NOT (~), and shifts (<<, >>).
- **UTF-8 Encoding Scheme**: Familiarity with the UTF-8 encoding rules, including how characters are encoded into one or more bytes.
- **Data Representation**: How to represent and work with data at the byte level.
- **List Manipulation in Python**: Iterating through lists, accessing list elements, and understanding list comprehensions.
- **Boolean Logic**: Applying logical operations to make decisions within the program.

## Usage

### Script

The script `utf8_validation.py` checks if a given dataset represents a valid UTF-8 encoding.

### Example

\`\`\`python
#!/usr/bin/python3
\"\"\"
UTF-8 Validation
\"\"\"

def validUTF8(data):
    \"\"\"
    Check if the data set represents a valid UTF-8 encoding.
    :param data: List of integers representing the bytes of the data set
    :return: True if data is a valid UTF-8 encoding, else False
    \"\"\"
    num_bytes = 0

    for num in data:
        bin_rep = format(num, '#010b')[-8:]

        if num_bytes == 0:
            if bin_rep[0] == '0':
                continue

            count_ones = 0
            for bit in bin_rep:
                if bit == '1':
                    count_ones += 1
                else:
                    break

            if count_ones == 1 or count_ones > 4:
                return False

            num_bytes = count_ones - 1
        else:
            if not (bin_rep[0] == '1' and bin_rep[1] == '0'):
                return False
            num_bytes -= 1

    return num_bytes == 0

if __name__ == "__main__":
    # Example data
    data = [197, 130, 1]  # This should return True
    print(validUTF8(data))
    
    data = [235, 140, 4]  # This should return False
    print(validUTF8(data))
\`\`\`

## How to Run

1. Clone the repository and navigate to the project directory.
2. Ensure the script `utf8_validation.py` is executable:
    \`\`\`sh
    chmod +x utf8_validation.py
    \`\`\`
3. Run the script with example data:
    \`\`\`sh
    ./utf8_validation.py
    \`\`\`

## Resources

- [Bitwise Operations in Python](https://www.w3schools.com/python/python_operators.asp)
- [UTF-8 Wikipedia](https://en.wikipedia.org/wiki/UTF-8)
- [The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/)

## Author

Kyanzi Hassan Musisi - [Kyanzi Hassan Musisi](https://www.x.com/hassan_kyanzi)


