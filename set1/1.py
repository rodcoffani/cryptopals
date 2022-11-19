from base64 import b64encode

def hex_to_base64(hex_string):
    return b64encode(bytes.fromhex(hex_string)).decode()

h_string= input("Enter hex string: ")
print(hex_to_base64(h_string))