import vigenerecipher

def main():

    print("-------------------")
    print("| Vigenere Cipher |")
    print("-------------------\n")

    vc = vigenerecipher.VigenereCipher()

    keyword = "CIPHERCI"

    plaintext = "VIGENERE"
    print(f'Plaintext:  {plaintext}')

    enciphered = vc.encipher(plaintext, keyword)
    print(f'Enciphered: {enciphered}')

    deciphered = vc.decipher(enciphered, keyword)
    print(f'Deciphered: {deciphered}')


main()