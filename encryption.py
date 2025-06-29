from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import base64
import json

def encrypt_data(data, validate_key):
    # Ensure the key is 16, 24, or 32 bytes for AES
    secret_key = validate_key.encode('utf-8')
    if len(secret_key) not in [16, 24, 32]:
        raise ValueError("Invalid key length. Key must be 16, 24, or 32 bytes long.")

    # Convert data to JSON and encode to bytes
    data_str = json.dumps(data)
    data_bytes = data_str.encode('utf-8')

    # Generate random IV (Initialization Vector)
    iv = get_random_bytes(16)

    # Perform AES encryption in CBC mode with PKCS7 padding
    cipher = AES.new(secret_key, AES.MODE_CBC, iv)
    encrypted_bytes = cipher.encrypt(pad(data_bytes, AES.block_size))

    # Combine IV and encrypted data (like in the JS code)
    combined_data = iv + encrypted_bytes

    # Encode to Base64 to mimic JS behavior
    encrypted_base64 = base64.b64encode(combined_data).decode('utf-8')
    return encrypted_base64



data ={
     
    "email_id":"aruna@sagasoft.xyz"

}


validate_key = "f-nJuoBDU%ZQQZF<"  
encrypted_data = encrypt_data(data, validate_key)
print("Encrypted Data:", encrypted_data)

