# file_integrity_checker.py

import hashlib

def calculate_hash(filepath):
    sha = hashlib.sha256()
    with open(filepath, 'rb') as f:
        while chunk := f.read(4096):
            sha.update(chunk)
    return sha.hexdigest()

file_path = "yourfile.txt"  # Replace with your file name
original_hash = calculate_hash(file_path)
print("Original Hash:", original_hash)

input("Edit the file and press Enter to re-check...")

new_hash = calculate_hash(file_path)
print("New Hash:", new_hash)

if original_hash != new_hash:
    print("🔴 File has been modified!")
else:
    print("🟢 File is unchanged.")