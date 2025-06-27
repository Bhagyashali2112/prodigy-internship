def caesar_cipher_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # Only shift alphabetic characters
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  # Keep non-alphabet characters unchanged
    return result

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)  # Just reverse the shift

def main():
    print("Welcome to the Caesar Cipher program!")
    choice = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").strip().lower()

    if choice not in ['encrypt', 'decrypt']:
        print("Invalid choice. Please type 'encrypt' or 'decrypt'.")
        return

    message = input("Enter your message: ")
    try:
        shift = int(input("Enter shift value (a number): "))
    except ValueError:
        print("Invalid shift value. Please enter an integer.")
        return

    if choice == 'encrypt':
        encrypted_message = caesar_cipher_encrypt(message, shift)
        print("Encrypted message:", encrypted_message)
    else:
        decrypted_message = caesar_cipher_decrypt(message, shift)
        print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    main()
