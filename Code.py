def caeser_cipher(text, shift, encrypt):
    result = ""

    shift %= 26 # Normalize the shift key value (0 - 25)

    if not encrypt:
        shift = -shift 
    
    for ch in text:
        if ch.isalpha():
            start = ord('A') if ch.isupper() else ord('a')  # To determine ASCII value
            ch_ASCII = ord(ch) - start
            # Apply the Caesar Cipher formula: C = (P + K) mod 26
            result += chr((ch_ASCII + shift) % 26 + start)
        else:
            result += ch
    
    return result


print("------ Welcome to Caesar Cipher Program! ------")
print()
print("Do you want to encrypt a plaintext or decrypt a ciphertext?")
operation = input("1: Encrypt\n2: Decrypt\nChoice: ")

encrypt = True
if operation.strip() == "2":
    encrypt = False

text = input("Enter the text you want to encrypt or decrypt: ")
shift = int(input("Enter the shift key (From 1 to 26): "))

print("\nResult:", caeser_cipher(text, shift, encrypt))
