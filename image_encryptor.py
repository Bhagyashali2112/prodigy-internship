from PIL import Image

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            # Encrypt each channel with a simple operation
            pixels[x, y] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)

    img.save(output_path)
    print("Encryption complete. Saved to", output_path)

def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            # Reverse the encryption operation
            pixels[x, y] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)

    img.save(output_path)
    print("Decryption complete. Saved to", output_path)

def main():
    choice = input("Enter 'e' to encrypt or 'd' to decrypt: ").lower()
    input_path = input("Enter the input image file path: ")
    output_path = input("Enter the output image file path: ")
    key = int(input("Enter the key (a number): "))

    if choice == 'e':
        encrypt_image(input_path, output_path, key)
    elif choice == 'd':
        decrypt_image(input_path, output_path, key)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
