def xor_hex_strings(hex_string1, hex_string2):
    return bytes([a ^ b for a, b in zip(bytes.fromhex(hex_string1), bytes.fromhex(hex_string2))]).hex()
    
h_string1= input("Enter hex string 1: ")
h_string2= input("Enter hex string 2: ")
xor_string= xor_hex_strings(h_string1, h_string2)

print(xor_string)