import string
import os

# ========== Constants ==========
ALPHABET = string.ascii_uppercase
DIGIT_FLIP = {'0': '0', '1': '9', '2': '8', '3': '7', '4': '6',
              '5': '5', '6': '4', '7': '3', '8': '2', '9': '1'}

# ========== Cipher Logic ==========
def rotate_char(c, shift):
    if c.upper() not in ALPHABET:
        return c
    idx = ALPHABET.index(c.upper())
    new_idx = (idx + shift) % 26
    new_char = ALPHABET[new_idx]
    return new_char if c.isupper() else new_char.lower()

def flip_digits(text):
    return ''.join(DIGIT_FLIP.get(ch, ch) for ch in text)

def nomem13_encode(text):
    encoded = []
    words = text.split()

    for word in words:
        if word.isdigit():
            encoded.append(flip_digits(word))
            continue

        if not word:
            continue

        anchor = word[0]
        shift = 13 if anchor.lower() in 'aeiou' else -13
        transformed = ""

        for ch in word:
            if ch.upper() == 'M':
                transformed += ch  # M stays the same
            elif ch.isalpha():
                transformed += rotate_char(ch, shift)
            elif ch.isdigit():
                transformed += DIGIT_FLIP.get(ch, ch)
            else:
                transformed += ch

        encoded.append(transformed)

    return "::k13:: " + ' '.join(encoded)

def nomem13_decode(text):
    if text.startswith("::k13:: "):
        text = text[8:]

    decoded = []
    words = text.split()

    for word in words:
        if word.isdigit():
            decoded.append(flip_digits(word))
            continue

        if not word:
            continue

        anchor = word[0]
        shift = -13 if anchor.lower() in 'aeiou' else 13
        transformed = ""

        for ch in word:
            if ch.upper() == 'M':
                transformed += ch
            elif ch.isalpha():
                transformed += rotate_char(ch, shift)
            elif ch.isdigit():
                transformed += DIGIT_FLIP.get(ch, ch)
            else:
                transformed += ch

        decoded.append(transformed)

    return ' '.join(decoded)

# ========== Interface ==========
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print("""
  ███╗   ██╗ ██████╗ ███╗   ███╗███████╗███╗   ███╗
  ████╗  ██║██╔═══██╗████╗ ████║██╔════╝████╗ ████║
  ██╔██╗ ██║██║   ██║██╔████╔██║█████╗  ██╔████╔██║
  ██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══╝  ██║╚██╔╝██║
  ██║ ╚████║╚██████╔╝██║ ╚═╝ ██║███████╗██║ ╚═╝ ██║
  ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═╝     ╚═╝
            🔒 Welcome to k.nomem13 Cipher 🔑
    """)

def main():
    while True:
        clear_screen()
        banner()
        print("1. Encode a message")
        print("2. Decode a message")
        print("3. Exit")
        choice = input("\nChoose an option [1/2/3]: ").strip()

        if choice == "1":
            msg = input("\nEnter the message to ENCODE: ")
            result = nomem13_encode(msg)
            print(f"\n🧬 Encoded Message:\n{result}")
        elif choice == "2":
            msg = input("\nEnter the message to DECODE: ")
            result = nomem13_decode(msg)
            print(f"\n🧬 Decoded Message:\n{result}")
        elif choice == "3":
            print("\n👋 Exiting the Cipher Lab. Stay stealthy, agent 13.")
            break
        else:
            print("\n❌ Invalid option. Try again!")

        input("\nPress Enter to continue...")

# Run the program
if __name__ == "__main__":
    main()
