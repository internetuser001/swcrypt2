import json

def load_key(key_path):
    with open(key_path, "r", encoding="utf-8") as f:
        key_input = f.read()
    temp_key = json.loads(key_input)
    return {int(k): v for k, v in temp_key.items()}

def encryptor(sequence, key):
    final = ""
    for p in sequence:
        final += str(key[ord(p)]) + "/"
    return final

def main():
    key_path = input("Enter the path to the key file: ")
    key = load_key(key_path)

    input_path = input("Enter the path to the file you want to encrypt: ")
    with open(input_path, "r", encoding="utf-8") as f:
        plaintext = f.read()

    encrypted_text = encryptor(plaintext, key)

    with open(input_path, "w", encoding="utf-8") as f:
        f.write(encrypted_text)

    print(f"Encryption complete. File '{input_path}' overwritten with encrypted data.")

if __name__ == "__main__":
    main()
