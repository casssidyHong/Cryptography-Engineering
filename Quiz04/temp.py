plaintext = "ATNYCUWEARESTRIVINGTOBEAGREATUNIVERSITYTHATTRANSCENDSDISCIPLINARYDIVIDESTOSOLVETHEINCREASINGLYCOMPLEXPROBLEMSTHATTHEWORLDFACESWEWILLCONTINUETOBEGUIDEDBYTHEIDEATHATWECANACHIEVESOMETHINGMUCHGREATERTOGETHERTHANWECANINDIVIDUALLYAFTERALLTHATWASTHEIDEATHATLEDTOTHECREATIONOFOURUNIVERSITYINTHEFIRSTPLACE"

print("Plaintext:\n", plaintext, sep='')

stream = ""
generator = '00000001'
while stream.__len__() < plaintext.__len__()*8:
    stream += generator[7]
    shift = (generator[0]=='1')
    generator = generator[1:] + '0'
    if shift:
        for i in [3,4,5,7]:
            if generator[i] == '1':
                generator = generator[:i] + '0' + generator[i+1:]
            else:
                generator = generator[:i] + '1' + generator[i+1:]


def string_to_binary(s):
    return ''.join(format(ord(c), '08b') for c in s)

binary_text = string_to_binary(plaintext)

def binary_to_string(b):
    return ''.join(chr(int(b[i:i+8], 2)) for i in range(0, len(b), 8))

def xor(a, b):
    return ''.join(str(int(a[i]) ^ int(b[i])) for i in range(len(a)))

cipher_text = xor(binary_text, stream)
print("Cipher text:\n", cipher_text, sep='')

for i in range(0, len(cipher_text), 8):
    print(cipher_text[i], end='')

recovered_text = binary_to_string(xor(cipher_text, stream))
print("\nRecovered text:\n", recovered_text, sep='')