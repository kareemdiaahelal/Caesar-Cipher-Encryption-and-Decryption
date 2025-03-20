def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    
    return result
# qq
# Main
print("Welcome to Caesar Cipher Program!")
print("=================================")
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))
mode = input("Type 'encrypt' or 'decrypt': ").lower()

output = caesar_cipher(message, shift, mode)
print(f"Result: {output}")
