def caesar_cipher(text, shift, mode='encode'):
    result = ""
    if mode == 'decode':
        shift = -shift

    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
        else:
            result += char
    return result

def main():
    while True:
        mode = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
        if mode not in ['encode', 'decode']:
            print("Invalid mode. Please choose 'encode' or 'decode'.")
            continue
        
        message = input("Enter your message: ")
        try:
            shift = int(input("Type the shift number: "))
        except ValueError:
            print("Shift must be a number. Please try again.")
            continue

        result = caesar_cipher(message, shift, mode)
        print(f"The {mode}d message is: {result}")

        again = input("Do you want to go again? Type 'yes' or 'no': ").lower()
        if again != 'yes':
            break

if __name__ == "__main__":
    main()
