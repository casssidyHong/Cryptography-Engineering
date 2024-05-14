import secrets

def generate_random_bytes(num_bytes):
    return bytes([secrets.randbits(8) for _ in range(num_bytes)])

if __name__ == "__main__":
    num_bytes = 1024 * 1024  # 1MB
    random_bytes = generate_random_bytes(num_bytes)
    
    with open('/Users/cassidy/Desktop/1_密碼工程/Quiz05/temp/sts-2.1.2/sts-2.1.2/random.bin', 'wb') as file:
        file.write(random_bytes)
