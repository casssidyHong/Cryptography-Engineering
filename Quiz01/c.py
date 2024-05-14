def manual_substitution(ciphertext, substitution_dict):
    # 对每个字母进行手动替代
    decrypted_text = ''.join([substitution_dict.get(char, char) for char in ciphertext])

    return decrypted_text

# 提供的密文
ciphertext = "C UYGHARMZ IUWMPRWIR GAIR YVRMP MBHMZWMPUM C VMMXWPE YV PYR VCZ ZMGYQMD VZYG CXCZG YP CPCXKTWPE CPD MBHXYZM RNM VXYYD YV CDQCPUMD OPYSXMDEM SNWUN MCUN KMCZ LZWPEI SWRN WR"

# 根据频率分析的结果手动替代
substitution_dict = {
    # j q
    'A': 'u',
    'B': 'x', 
    'C': 'a',
    'D': 'd',
    'E': 'g',
    'F': '_',
    'G': 'm',
    'H': 'p',
    'I': 's',
    'J': '_', 
    'K': 'y',
    'L': 'b',
    'M': 'e',
    'N': 'h',
    'O': 'k',
    'P': 'n',
    'Q': 'v',
    'R': 't',
    'S': 'w',
    'T': 'z',
    'U': 'c',
    'V': 'f',
    'W': 'i',
    'X': 'l',
    'Y': 'o',
    'Z': 'r'
}


# 手动替代
decrypted_message = manual_substitution(ciphertext, substitution_dict)

# 输出解密后的文本
print("Decrypted Message:")
print(decrypted_message)
