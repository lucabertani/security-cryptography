import struct

from Alphabet import Alphabet


class StreamAlphabetic:
    def __init__(self, cipher_path):
        self.cipher_path = cipher_path

        f = open(cipher_path, "r")
        self.cipher = f.read()
        f.close()

        print(self.cipher)

        self.dict_replace = {}
        self.decrypted = ""

    def crack_cipher(self):
        # semplicemente tento con tutti i caratteri dell'alfabeto
        dict = {}
        for k in Alphabet.CHARACTERS:
            plain_text = self.autokey_decrypt(k, self.cipher)

            # essendo in inglese, mi aspetto che il testo in chiaro sia "vicino" alla distribuzione di occorenza
            # delle parole inglese, quindi il decriptato più vicino sarà quello corretto
            distance = self.get_proximity(plain_text)
            dict[distance] = {k, plain_text}

        dict_sorted = sorted(dict.items())
        return next(iter(dict_sorted))


    def autokey_encrypt(self, key, plain_text):
        # Ez(x) = x + z mod 26
        k = key
        cipher = ""
        for plain_char in plain_text:
            pos_x = Alphabet.CHARACTERS.find(plain_char)
            pos_z = Alphabet.CHARACTERS.find(k)
            new_pos = (pos_x + pos_z) % 26
            cipher += Alphabet.CHARACTERS[new_pos]
            k = plain_char

        return cipher

    def autokey_decrypt(self, key, cipher):
        # Dz(y) = y - z mod 26
        k = key
        plain_text = ""
        for cipher_char in cipher:
            pos_y = Alphabet.CHARACTERS.find(cipher_char)
            pos_z = Alphabet.CHARACTERS.find(k)
            new_pos = (pos_y - pos_z) % 26
            plain_char = Alphabet.CHARACTERS[new_pos]
            plain_text += plain_char
            k = plain_char

        return plain_text

    def get_proximity(self, ciphertext):
        dict = {}
        N = len(ciphertext)

        for letter in Alphabet.CHARACTERS:
            dict[letter] = ciphertext.count(letter) / N

        distance = 0
        for letter in Alphabet.WORD_USAGE:
            usage = float(Alphabet.WORD_USAGE[letter])
            usage_plain_text = float(dict[letter])

            # usage_a = struct.pack('d', usage)
            # print(f"usage_a {usage_a}")

            # distance += self.xor_float(usage_plain_text, usage)
            distance += abs(usage_plain_text - usage)



        return distance

    def xor_float(self, f1, f2):
        f1 = int(''.join(hex(ord(e))[2:] for e in struct.pack('d', f1)), 16)
        f2 = int(''.join(hex(ord(e))[2:] for e in struct.pack('d', f2)), 16)
        xor = f1 ^ f2
        xor = "{:016x}".format(xor)
        xor = ''.join(chr(int(xor[i:i + 2], 16)) for i in range(0, len(xor), 2))
        return struct.unpack('d', xor)[0]



