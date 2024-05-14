def manual_substitution(ciphertext, substitution_dict):
    # 对每个字母进行手动替代
    decrypted_text = ''.join([substitution_dict.get(char, char) for char in ciphertext])

    return decrypted_text

# 提供的密文
ciphertext = "U AKENCZGT WASGHZSWZ ECWZ KJZGH GLNGTSGHAG U JGGBSHM KJ HKZ JUT TGEKFGD JTKE UBUTE KH UHUBORSHM UHD GLNBKTG ZPG JBKKD KJ UDFUHAGD YHKIBGDKG HPSAP GUAP OGUT XTHSMW ISTP SZ"

# 根据频率分析的结果手动替代
substitution_dict = {
    # b h j k q w
    'A': '_',
    'B': '_',
    'C': '_',
    'D': '_',
    'E': '_',
    'F': '_',
    'G': '_',
    'H': '_',
    'I': '_',
    'J': '_',
    'K': '_',
    'L': '_',
    'M': '_',
    'N': '_',
    'O': '_',
    'P': '_',
    'Q': '_',
    'R': '_',
    'S': '_',
    'T': '_',
    'U': '_',
    'V': '_',
    'W': '_',
    'X': '_',
    'Y': '_',
    'Z': '_',
}


# 手动替代
decrypted_message = manual_substitution(ciphertext, substitution_dict)

# 输出解密后的文本
print("Decrypted Message:")
print(decrypted_message)
