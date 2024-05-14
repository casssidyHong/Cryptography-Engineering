def calculate_letter_frequencies(ciphertext):
    letter_frequencies = {}

    for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        letter_frequencies[char] = 0

    for char in ciphertext:
        if char.isalpha():
            char = char.upper()

            letter_frequencies[char] = letter_frequencies.get(char, 0) + 1

    return letter_frequencies

def main():
    ciphertext = input("Enter the ciphertext: ")
    frequencies = calculate_letter_frequencies(ciphertext)

    print("\nLetter frequencies in the ciphertext: ")
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print(f"{letter}: {frequencies[letter]}")

if __name__ == "__main__":
    main()
