# Implementation of the Vigenère cipher in python
# References https://en.wikipedia.org/wiki/Vigenere_cipher

import string
import random

def convertToAllCaps(string: str) -> str:
    """
    Converts a given string into all capital letters and removes any special characters
    
    Parmeters
    ----------
    string: str
        string to be processed
    """
    res = ''
    for char in string:
        if char.isalpha():
            res += char.upper()
    return res

def keyConvolution(key: str, length: int) -> str:
    """
    Either trim or repeat key until it matches the length of the plaintext or ciphertext.

    Parmeters
    ----------
    key: str,
        cipher key
    length: int
        desired length
    """
    key = convertToAllCaps(key)
    if length <= len(key):
        return key[0:length]
    else: 
        remainder = length % len(key)
        repeat = int((length-remainder)/len(key))
        return key*repeat + key[0:remainder]
    
def keygen(length: int = 16) -> str:
    """
    generate keys

    Parmeters
    ----------
    length: int, default 16
        number of letters in the cipher key
    """
    print("Generating key...")
    key = ''.join(random.choice(string.ascii_uppercase) for _ in range(length))
    
    print(key+'\n')
    return key

def encrypt(key: str, plaintext: str) -> str:
    """
    encrypt a given plaintext message with a key using the vigenere cipher

    Parmeters
    ----------
    key: str,
        cipher key
    plaintext: str
        text to be encrypted
    """
    print("Encrypting...")
    plaintext = convertToAllCaps(plaintext)
    print(plaintext)
    key = keyConvolution(key, len(plaintext))
    print(key)
    
    ciphertext = ''
    for i in range(len(plaintext)):
        plaintextIndex = string.ascii_uppercase.index(plaintext[i])
        keyIndex = string.ascii_uppercase.index(key[i])
        ciphertextIndex = (plaintextIndex + keyIndex) % 26
        ciphertext += string.ascii_uppercase[ciphertextIndex]   

    print(ciphertext+'\n')          
    return ciphertext

def decrypt(key: str, ciphertext: str) -> str:
    """
    decrypt a given ciphertext message with a known cipher key

    Parmeters
    ----------
    key: str,
        cipher key
    ciphertext: str
        encrypted text to be decrpyted
    """
    print('Decrypting...')
    print(ciphertext)
    key = keyConvolution(key, len(ciphertext))
    print(key)
    
    plaintext = ''
    for i in range(len(ciphertext)):
        ciphertextIndex = string.ascii_uppercase.index(ciphertext[i])
        keyIndex = string.ascii_uppercase.index(key[i])
        plaintextIndex = (ciphertextIndex - keyIndex) % 26
        plaintext += string.ascii_uppercase[plaintextIndex]

    print(plaintext+'\n')             
    return plaintext

if __name__ == '__main__':
    print("-------- Example 1 --------")
    key = keygen()
    ciphertext = encrypt(key, "Hello my name is Alex Perrin")
    plaintext = decrypt(key, ciphertext)

    print("-------- Example 2 ---------")
    key = "LEMON"
    ciphertext = encrypt(key, "attackatdawn")
    plaintext = decrypt(key, ciphertext)
