import pytest

def hex_to_bytes(hex_string):
    """Convert a hex string to bytes."""
    return bytes.fromhex(hex_string)

def bytes_to_base64(byte_data):
    """Manually encode bytes to base64 (without using built-in libraries)."""
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    binary_string = ''.join(f'{byte:08b}' for byte in byte_data)  # Convert bytes to binary
    
    # Pad binary string so its length is a multiple of 6
    while len(binary_string) % 6 != 0:
        binary_string += '0'
    
    # Convert each 6-bit chunk to a base64 character
    base64_string = ''.join(base64_chars[int(binary_string[i:i+6], 2)] for i in range(0, len(binary_string), 6))
    
    # Add padding if necessary
    while len(base64_string) % 4 != 0:
        base64_string += '='
    
    return base64_string

def test_hex_to_bytes():
    assert hex_to_bytes("49276d") == b"I'm"
    assert hex_to_bytes("68656c6c6f") == b"hello"
    assert hex_to_bytes("776f726c64") == b"world"

def test_bytes_to_base64():
    assert bytes_to_base64(b"I'm") == "SSdt"
    assert bytes_to_base64(b"hello") == "aGVsbG8="
    assert bytes_to_base64(b"world") == "d29ybGQ="

def test_full_conversion():
    hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b652061205047"
    expected_base64 = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgdEcn"
    assert bytes_to_base64(hex_to_bytes(hex_string)) == expected_base64

if __name__ == "__main__":
    pytest.main()
