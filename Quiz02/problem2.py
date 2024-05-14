import hashlib
import time

def generateHash():
    with open('video.mp4', 'rb') as f:
        content = f.read()

        # MD5
        timeStart = time.time()
        md5 = hashlib.md5()
        for i in range(0, len(content), 8192):
            md5.update(content[i:i + 8192])
        md5 = md5.hexdigest()
        timeEnd = time.time()
        md5_speed = timeEnd - timeStart

        # SHA-1
        timeStart = time.time()
        sha1 = hashlib.sha1(content).hexdigest()
        timeEnd = time.time()
        sha1_speed = timeEnd - timeStart

        # SHA-224
        timeStart = time.time()
        sha224 = hashlib.sha224(content).hexdigest()
        timeEnd = time.time()
        sha224_speed = timeEnd - timeStart

        # SHA-256
        timeStart = time.time()
        sha256 = hashlib.sha256(content).hexdigest()
        timeEnd = time.time()
        sha256_speed = timeEnd - timeStart

        # SHA-512
        timeStart = time.time()
        sha512 = hashlib.sha512(content).hexdigest()
        timeEnd = time.time()
        sha512_speed = timeEnd - timeStart

        # SHA-3-224
        timeStart = time.time()
        sha3_224 = hashlib.sha3_224(content).hexdigest()
        timeEnd = time.time()
        sha3_224_speed = timeEnd - timeStart

        # SHA-3-256
        timeStart = time.time()
        sha3_256 = hashlib.sha3_256(content).hexdigest()
        timeEnd = time.time()
        sha3_256_speed = timeEnd - timeStart

        # SHA-3-512
        timeStart = time.time()
        sha3_512 = hashlib.sha3_512(content).hexdigest()
        timeEnd = time.time()
        sha3_512_speed = timeEnd - timeStart

    # 印出速度最快的方法
    speeds = {
        'MD5': md5_speed,
        'SHA-1': sha1_speed,
        'SHA-224': sha224_speed,
        'SHA-256': sha256_speed,
        'SHA-512': sha512_speed,
        'SHA-3-224': sha3_224_speed,
        'SHA-3-256': sha3_256_speed,
        'SHA-3-512': sha3_512_speed
    }

    fastest_algorithm = min(speeds, key=speeds.get)
    print(f"The fastest algorithm is: {fastest_algorithm}")

    ranked_algorithms = sorted(speeds, key=speeds.get, reverse=False)
    print("Ranking of hash functions by speed:")
    for i, algorithm in enumerate(ranked_algorithms, start=1):
        print(f"{i}. {algorithm}: {speeds[algorithm]} seconds")

generateHash()