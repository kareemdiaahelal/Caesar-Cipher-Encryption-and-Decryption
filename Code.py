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

def get_valid_shift():
    while True:
        try:
            shift = int(input("Enter the shift key (From 1 to 26): "))
            if 1 <= shift <= 26:
                return shift
            else:
                raise ValueError

        except ValueError:
            print("Please enter a valid integer for the shift key!")

def get_operation():
    while True:
        print("Do you want to encrypt a plaintext or decrypt a ciphertext?")
        operation = input("1: Encrypt\n2: Decrypt\nChoice: ").strip()

        if operation == "1":
            return True
        elif operation == "2":
            return False
        else:
            print("Invalid choice. Please choose 1 for Encrypt or 2 for Decrypt!")

def main():
    print("------ Welcome to Caesar Cipher Program! ------\n")

    text = input("Enter the text you want to encrypt or decrypt: ")
    shift = get_valid_shift()
    encrypt = get_operation()


    print("\nResult:", caeser_cipher(text, shift, encrypt))


if __name__ == "__main__":
    main()