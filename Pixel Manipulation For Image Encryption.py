from PIL import Image
import random

# Encrypt the image using simple pixel manipulation (XOR or swapping pixels)
def encrypt_image(input_path, output_path, key=42):
    img = Image.open(input_path)
    pixels = img.load()  # Load the pixels

    # Get image dimensions
    width, height = img.size

    # Loop over each pixel and apply an XOR operation to each channel (R, G, B)
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            
            # Apply XOR with the key to each color channel
            r = r ^ key
            g = g ^ key
            b = b ^ key

            # Set the encrypted pixel value
            pixels[x, y] = (r, g, b)
    
    # Save the encrypted image
    img.save(output_path)
    print("Image encrypted and saved as", output_path)

# Decrypt the image by reversing the XOR operation
def decrypt_image(input_path, output_path, key=42):
    img = Image.open(input_path)
    pixels = img.load()  # Load the pixels

    # Get image dimensions
    width, height = img.size

    # Loop over each pixel and apply the XOR operation to each channel (R, G, B)
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            
            # Reverse the XOR with the same key to get the original color values
            r = r ^ key
            g = g ^ key
            b = b ^ key

            # Set the decrypted pixel value
            pixels[x, y] = (r, g, b)
    
    # Save the decrypted image
    img.save(output_path)
    print("Image decrypted and saved as", output_path)

# Example usage
if __name__ == "__main__":
    input_image = "panda.jpg"  # Path to the image you want to encrypt
    encrypted_image = "encrypted_image.jpg"  # Path to save the encrypted image
    decrypted_image = "decrypted_image.jpg"  # Path to save the decrypted image

    # Encrypt the image
    encrypt_image(input_image, encrypted_image)

    # Decrypt the image
    decrypt_image(encrypted_image, decrypted_image)
