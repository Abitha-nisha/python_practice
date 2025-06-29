from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64
import os
import json

def decrypt_data(encrypted_data, key):
    # Convert key from UTF-8
    secret_key = key.encode('utf-8')

    # Ensure the key length is 16, 24, or 32 bytes for AES
    secret_key = secret_key.ljust(32, b'\0')[:32]  # Pad or trim to 32 bytes

    # Decode Base64
    combined = base64.b64decode(encrypted_data)

    # Extract IV (first 16 bytes)
    iv = combined[:16]

    # Extract encrypted text
    encrypted = combined[16:]

    # Decrypt using AES (CBC mode)
    cipher = AES.new(secret_key, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(encrypted), AES.block_size)

    # Convert bytes to JSON
    return json.loads(decrypted.decode('utf-8'))

# Example Usage
VITE_ENCRYPT_KEY = "f-nJuoBDU%ZQQZF<"  # Should be same as used in encryption
encrypted_text = "oKOwcSUrQTjI7v0oxWN1IHIv3pfrn3fy1Ln3vu7HdxckCjNJSErYHtRyFSiC9tbgC6qSYm7A87i91qc0NsU/gCcFwBp2WRTw6VYr9UeEgdngydkS5j753rww1pSFk1r/KVFq23Z3ujfDfK7Z1RZAXhLVdH2rheBVOvvkOYEfeDgQCcVr7uFyV/1ckCANl0AA83CawHHVy0VWpBsXUbFY3d24zU2KxvgY2c663cHFOTTs4unRJ3dkMXutfgCRdQmM853cbBwcKGHkZtUbRNrQjcGf/tpDq3RlqaQfKipU6Uc="  # Replace with the actual encrypted output

decrypted_data = decrypt_data(encrypted_text, VITE_ENCRYPT_KEY)
print("Decrypted Data:", decrypted_data)