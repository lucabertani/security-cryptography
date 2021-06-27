from StreamAlphabetic import StreamAlphabetic

if __name__ == '__main__':
    stream_alphabetic = StreamAlphabetic("resources/cipher.txt")

    # test AutoKey
    cipher = stream_alphabetic.autokey_encrypt("B", "CIAOMONDO")
    print(f"Cipher: {cipher}")

    plain_text = stream_alphabetic.autokey_decrypt("B", cipher)
    print(f"Plain text: {plain_text}")

    # decriptazione
    decrypted = stream_alphabetic.crack_cipher()
    print(f"Decrypted: {decrypted[1]} with distance from english {decrypted[0]}")

    # AUGUSTE KERCKHOFFS WAS A DUTCH LINGUIST AND CRYPTOGRAPHER



