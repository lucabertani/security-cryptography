from AESAlgorithm import process_key, encrypt, decrypt, decrypt_eq

if __name__ == '__main__':
    # aes_alphabetic = AESAlphabetic("resources/cipher.txt")

    # r = aes_alphabetic.AESmult(0b11010011, 0b00111010, True)
    # r = aes_alphabetic.AESmult(0b0, 0b00111010, True)
    # print(r, r, bin(r))

    plain_text = "00112233445566778899aabbccddeeff"
    plain_key = "000102030405060708090a0b0c0d0e0f"

    block = process_key(plain_text)
    key = process_key(plain_key)
    # encrypt(block, key, 4, 4, 10)

    plain_cipher = "69c4e0d86a7b0430d8cdb78070b4c55a"
    cipher = process_key(plain_cipher)
    key = process_key(plain_key)

    # decrypt(cipher, key, 4, 4, 10)
    decrypt_eq(cipher, key, 4, 4, 10)

    # aes = AESAlgorithm(key, plain_text)
    # aes.encrypt()



