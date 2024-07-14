from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import json
import base64
import datetime

def encrypt_file(input_file, output_file, key, duration_hours):
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv

    with open(input_file, 'rb') as f:
        plaintext = f.read()

    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

    encryption_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    result = {
        'iv': base64.b64encode(iv).decode('utf-8'),
        'ciphertext': base64.b64encode(ciphertext).decode('utf-8'),
        'date': encryption_date,
        'duration_hours': duration_hours,
    }

    with open(output_file, 'w') as f:
        json.dump(result, f)

# Example usage
input_file = 'anna.rtf'
output_file = 'encrypted.json'
key = get_random_bytes(16)
duration_hours = 1  # Set the duration for which the encryption is valid

print(f'Encryption Key (keep this safe and embed in your decryption script): {base64.b64encode(key).decode("utf-8")}')
encrypt_file(input_file, output_file, key, duration_hours)