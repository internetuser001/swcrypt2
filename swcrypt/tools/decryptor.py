import json

def load_key(key_path):
    with open(key_path, "r", encoding="utf-8") as f:
        key_input = f.read()
    temp_key = json.loads(key_input)
    # Reverse the key dictionary: value -> ASCII code
    return {v: int(k) for k, v in temp_key.items()}

def decryptor(encrypted_sequence, reverse_key):
    encrypted_values = encrypted_sequence.strip("/").split("/")
    decrypted_chars = []
    for val in encrypted_values:
        if val == '':
            continue
        try:
            num = int(val)
        except ValueError:
            raise ValueError(f"Invalid number format: {val}")

        ascii_code = reverse_key.get(num)
        if ascii_code is None:
            raise ValueError(f"Encrypted value {val} not found in key!")
        decrypted_chars.append(chr(ascii_code))

    return "".join(decrypted_chars)

def main():
    key_path = input("Enter the path to the key file: ")
    encrypted_file_path = input("Enter the path to the encrypted file: ")

    reverse_key = load_key(key_path)

    with open(encrypted_file_path, "r", encoding="utf-8") as f:
        encrypted_sequence = f.read()

    decrypted_text = decryptor(encrypted_sequence, reverse_key)

    # Overwrite the encrypted file with decrypted content
    with open(encrypted_file_path, "w", encoding="utf-8") as f:
        f.write(decrypted_text)

    print(f"Decryption complete. File '{encrypted_file_path}' has been overwritten with decrypted data.")

if __name__ == "__main__":
    main()



