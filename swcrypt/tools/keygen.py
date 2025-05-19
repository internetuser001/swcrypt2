from random import randint
import json

def generate_key():
    # Generate keys for all Unicode code points (0 to 1,114,111)
    key = {i: randint(0, 10**20) for i in range(0, 1114112)}
    return key

def main():
    key = generate_key()
    json_key = json.dumps({str(k): v for k, v in key.items()})
    with open("key.txt", "w", encoding="utf-8") as f:
        f.write(json_key)
    print("Key generated and saved to 'key.txt'. Keep it safe!")

if __name__ == "__main__":
    main()
