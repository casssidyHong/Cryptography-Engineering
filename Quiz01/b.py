def linear_substitution(ciphertext, a, b):
    decrypted_text = ''
    for char in ciphertext:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.upper()

            x = ord(char) - ord('A')

            decrypted_x = (a * x + b) % 26
            decrypted_x  = int(decrypted_x)

            decrypted_char = chr(decrypted_x + ord('A'))

            decrypted_char = decrypted_char if is_upper else decrypted_char.lower()

            decrypted_text += decrypted_char
        else:
            decrypted_text += char

    return decrypted_text

ciphertext = "U AKENCZGT WASGHZSWZ ECWZ KJZGH GLNGTSGHAG U JGGBSHM KJ HKZ JUT TGEKFGD JTKE UBUTE KH UHUBORSHM UHD GLNBKTG ZPG JBKKD KJ UDFUHAGD YHKIBGDKG HPSAP GUAP OGUT XTHSMW ISTP SZ"

a =   # 选择合适的值
b = 3  # 选择合适的值
decrypted_message = linear_substitution(ciphertext, a, b)

print("Decrypted Message:")
print(decrypted_message)
