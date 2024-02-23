# Name: pararambha Shrestha
# University number: 2408419
import os

letters = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(line, key):
    ciphertext = ''
    for letter in line:
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
                ciphertext += letter
            else:
                newIndex = (index + key) % 26
                ciphertext += letters[newIndex]
        else:
            ciphertext += ' '
    return ciphertext

def decrypt(line, key):
    ciphertext = ''
    for letter in line:
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
                ciphertext += letter
            else:
                newIndex = (index - key) % 26
                ciphertext += letters[newIndex]
        else:
            ciphertext += ' '
    return ciphertext

def shift():
    while True:
        key = input("What is the shift number: ")
        if key.isdigit():
            return int(key)
        else:
            print("Invalid shift")

def write_messages(ciphertext):
    filename = "result.txt"
    with open(filename, "w") as file:
        for message in ciphertext:
            file.write(message)
    print(f"Output written to: {filename}")
    return filename

def is_file(filename):
    return os.path.exists(filename)

def process_file(filename, mode):
    ciphertext = []
    if is_file(filename):
        key = shift()
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if mode == 'e':
                    encrypted = encrypt(line, key)
                    ciphertext.append(encrypted)
                elif mode == 'd':
                    decrypted = decrypt(line, key)
                    ciphertext.append(decrypted)
                else:
                    print("Invalid mode")
                    return []
        write_messages(ciphertext)
        return ciphertext
    else:
        print(f"Invalid file: '{filename}' not found.")
        return []

def welcome():
    print("Welcome to the Caesar Cipher. \nThis program encrypts and decrypts text with the Caesar Cipher.")

def message_or_file():
    while True:
        mode = input("Enter 'e' for encryption or 'd' for decryption: ")
        if mode in ['e', 'd']:
            while True:
                file_format = input("Enter 'f' for file or 'c' for console: ")
                if file_format in ['f', 'c']:
                    while True:
                        if file_format == "f":
                                filename = input("Enter a filename: ")
                                if is_file(filename):
                                    process_file(filename, mode)
                                    break
                                else: 
                                    print("Invalid Filename.")
                                break
                        else:
                            line = input("What message would you like to encrypt/decrypt: ")
                            key = shift()
                            if mode == 'e':
                                result = encrypt(line, key)
                                print(f"Encrypted message: {result}")
                            else:
                                result = decrypt(line, key)
                                print(f"Decrypted message: {result}")
                            break
                else:
                    print("Invalid format.")
                break
        else:
            print("Invalid mode.")
        break
    
def main():
    welcome()
    message_or_file()
    while True:
        repeat = input("Do you want to encrypt or decrypt another message? (y/n): ").lower()
        if repeat == 'n':
            print("Thanks for using the program, goodbye!")
            break
        elif repeat == 'y':
            message_or_file()
        else:
            print("Invalid input. Exiting.")
            break

main()
