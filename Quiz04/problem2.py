# a) Please use x8 + x4 + x3 + x2 + 1 as a characteristic polynomial to write a Python program 
#    to encrypt the following plaintext message with the initial key 00000001, 
#    then decrypt it to see if your encryption is correct.

import numpy as np

plaintext = "ATNYCUWEARESTRIVINGTOBEAGREATUNIVERSITYTHATTRANSCENDSDISCIPLINARYDIVIDESTOSOLVETHEINCREASINGLYCOMPLEXPROBLEMSTHATTHEWORLDFACESWEWILLCONTINUETOBEGUIDEDBYTHEIDEATHATWECANACHIEVESOMETHINGMUCHGREATERTOGETHERTHANWECANINDIVIDUALLYAFTERALLTHATWASTHEIDEATHATLEDTOTHECREATIONOFOURUNIVERSITYINTHEFIRSTPLACE"
key = 0b00000001

print("Plaintext:", plaintext)

# print("\nPart a: ")

def lfsr(seed, characteristic_polynomial, length):
    state = seed
    keystream = []
    for _ in range(length):
        keystream.append(state & 1)
        feedback = 0
        for i, coeff in enumerate(characteristic_polynomial):
            feedback ^= (state >> i) & coeff
        state = (state >> 1) | (feedback << (len(characteristic_polynomial) - 1))
    return keystream

def a_encrypt(plaintext, key):
    keystream = lfsr(key, [1, 0, 0, 0, 1, 1, 1, 0, 1], len(plaintext))
    ciphertext = [chr(ord(plaintext[i]) ^ keystream[i]) for i in range(len(plaintext))]
    return ''.join(ciphertext)

def a_decrypt(ciphertext, key):
    keystream = lfsr(key, [1, 0, 0, 0, 1, 1, 1, 0, 1], len(ciphertext))
    plaintext = [chr(ord(ciphertext[i]) ^ keystream[i]) for i in range(len(ciphertext))]
    return ''.join(plaintext)

encrypted_text = a_encrypt(plaintext, key)


decrypted_text = a_decrypt(encrypted_text, key)
print("Decrypted text:", decrypted_text)

# print("\n Part c: ")

# # c) Extra credit: 

# def lfsr(seed, characteristic_polynomial, length):
#     state = seed
#     keystream = []
#     for _ in range(length):
#         keystream.append(state & 1)
#         feedback = 0
#         for i, coeff in enumerate(characteristic_polynomial):
#             feedback ^= (state >> i) & coeff
#         state = (state >> 1) | (feedback << (len(characteristic_polynomial) - 1))
#     return keystream

# def c_encrypt(plaintext, key):
#     keystream = lfsr(key, [1, 0, 0, 0, 1, 1, 0, 1, 1], len(plaintext))
#     ciphertext = [ord(plaintext[i]) ^ keystream[i] for i in range(len(plaintext))]
#     return ciphertext

# def solve_linear_equations(plaintext, ciphertext, initial_key):
#     equations = []
#     for i in range(len(plaintext)):
#         equation = [0] * 9
#         equation[0] = int(format(initial_key, '08b')[0])  # MSB of initial key
#         for j in range(1, 9):
#             equation[j] = int(format(plaintext[i], '08b')[j-1]) ^ int(format(ciphertext[i], '08b')[j-1])
#         equations.append(equation)
    
#     A = np.array([eq[1:] for eq in equations])
#     b = np.array([eq[0] for eq in equations])
    
#     # Solve matrix equation Ax = b
#     x = np.linalg.lstsq(A, b, rcond=None)[0]
#     characteristic_polynomial = [1] + [int(round(coeff)) for coeff in x]
    
#     return characteristic_polynomial

# def c_decrypt(ciphertext, key):
#     keystream = lfsr(key, [1, 0, 0, 0, 1, 1, 0, 1, 1], len(ciphertext))
#     decrypted_plaintext = [ciphertext[i] ^ keystream[i] for i in range(len(ciphertext))]
#     return decrypted_plaintext

# # Encrypt the plaintext
# ciphertext = c_encrypt(plaintext, key)

# # Solve linear equations to find characteristic polynomial
# characteristic_polynomial = solve_linear_equations([ord(c) for c in plaintext], ciphertext, key)
# print("Characteristic polynomial:", characteristic_polynomial)

# # 加密並輸出密文
# print("加密後的文字：", ''.join([chr(c) for c in ciphertext]))

# # 解密並輸出解密後的明文
# decrypted_ciphertext = c_decrypt(ciphertext, key)
# print("解密後的文字：", ''.join([chr(c) for c in decrypted_ciphertext]))
