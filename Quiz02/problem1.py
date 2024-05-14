import hashlib
import sys
import time

def read_file():
    file = open("password.txt","r")
    look = file.read()

    arr = []
    arr = look.split()
    return file, arr

def findMatch(x):
    print(f"Hash: {x}")
    temp = read_file()
    file = temp[0]
    arr = temp[1]
    count = 0
    timeStart = time.time()
    for word in arr:
        # 使用 hashlib 庫的 sha1 函數計算雜湊
        daHash = hashlib.sha1(word.encode())  # 將字串轉換為位元組
        miHash = daHash.hexdigest()
        if miHash == x:
            file.close()
            timeEnd = time.time()
            print(f"Password: {word}")
            print(f"Took {str(count)} attempts to crack input hash. Time Taken: {str(timeEnd - timeStart)}\n")
            break
        count += 1
    return word

def findSalt(x):
    temp = read_file()
    file = temp[0]
    arr = temp[1]
    count = 0
    timeStart = time.time()
    for word in arr:
        # 使用 hashlib 庫的 sha1 函數計算雜湊
        daHash = hashlib.sha1(word.encode())  # 將字串轉換為位元組
        miHash = daHash.hexdigest()
        if miHash == x:
            file.close()
            break
        count += 1
    return word, timeStart

def findMatch2(y, w, timeStart):
    print(f"Hash: {w}")
    temp = read_file()
    file = temp[0]
    arr = temp[1]
    mainHash = w
    concat = y
    count = 0
    for word in arr:
        addCheck = concat + word
        daHash = hashlib.sha1(addCheck.encode())  # 將字串轉換為位元組
        miHash = daHash.hexdigest()
        if miHash == mainHash:
            file.close()
            timeEnd = time.time()
            print(f"Password: {y + word}")
            print(f"Took {str(count)} attempts to crack input hash. Time Taken: {str(timeEnd - timeStart)}\n")
            break
        count += 1
    return word

easy = "ef0ebbb77298e1fbd81f756a4efc35b977c93dae"
medium = "0bc2f4f2e1f8944866c2e952a5b59acabd1cebf2"
leet = "9d6b628c1f81b4795c0266c0f12123c1e09a7ad3"
leet_salt = "dfc3e4f0b9b5fb047e9be9fb89016f290d2abb06"
extra = "44ac8049dd677cb5bc0ee2aac622a0f42838b34d"
extra_salt = "44ac8049dd677cb5bc0ee2aac622a0f42838b34d"

findMatch(easy)
findMatch(medium)
temp = findSalt(leet_salt)
salt = temp[0]
startTime = temp[1]
findMatch2(salt, leet, startTime)
