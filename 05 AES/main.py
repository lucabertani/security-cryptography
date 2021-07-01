from AESAlgorithm import AESAlgorithm
from AESAlphabetic import AESAlphabetic

if __name__ == '__main__':
    # aes_alphabetic = AESAlphabetic("resources/cipher.txt")

    # r = aes_alphabetic.AESmult(0b11010011, 0b00111010, True)
    # r = aes_alphabetic.AESmult(0b0, 0b00111010, True)
    # print(r, r, bin(r))

    plain_text = "00112233445566778899aabbccddeeff"
    key = "000102030405060708090a0b0c0d0e0f"
    aes = AESAlgorithm(key, plain_text)
    aes.encrypt()



