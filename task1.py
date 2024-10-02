# Function to encrypt text using Caesar Cipher
def caesar_encrypt(text, shift):
    encrypted_text = ""
    
    for char in text:
        # Encrypt uppercase characters
        if char.isupper():
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        # Non-alphabetic characters remain unchanged
        else:
            encrypted_text += char
    
    return encrypted_text

# Function to decrypt text using Caesar Cipher
def caesar_decrypt(text, shift):
    decrypted_text = ""
    
    for char in text:
        # Decrypt uppercase characters
        if char.isupper():
            decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
        # Decrypt lowercase characters
        elif char.islower():
            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        # Non-alphabetic characters remain unchanged
        else:
            decrypted_text += char
    
    return decrypted_text

# Main program
def main():
    # Input from user
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))
    
    # Encrypt the message
    encrypted_message = caesar_encrypt(message, shift)
    print(f"Encrypted message: {encrypted_message}")
    
    # Decrypt the message
    decrypted_message = caesar_decrypt(encrypted_message, shift)
    print(f"Decrypted message: {decrypted_message}")

# Run the program
if __name__ == "__main__":
    main()
