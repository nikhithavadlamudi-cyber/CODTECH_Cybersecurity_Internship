# aes_encryption.py

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def pad(text):
    while len(text) % 16 != 0:
        text += ' '
    return text

key = get_random_bytes(32)
cipher = AES.new(key, AES.MODE_ECB)

message = "This is a secret"
padded = pad(message)
encrypted = cipher.encrypt(padded.encode())

print("🔒 Encrypted:", encrypted)

decrypted = cipher.decrypt(encrypted).decode().strip()
print("🔓 Decrypted:", decrypted)