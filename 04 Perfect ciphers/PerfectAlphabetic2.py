from Color import Color


class PerfectAlphabetic2:
    def __init__(self, cipher_path):
        self.cipher_path = cipher_path

        f = open(cipher_path, "r")
        self.cipher = f.read()
        f.close()

        # print(self.cipher)

        self.c1, self.c2, self.c3, self.c4 = self.cipher.split('\n')

        print(self.c1)
        print(self.c2)
        print(self.c3)
        print(self.c4)
        print("")

    def crack_cipher(self):
        hex1 = self.c1
        hex2 = self.c2
        hex3 = self.c3
        hex4 = self.c4

        res_hex12 = self.xor(hex1, hex2)
        res_hex13 = self.xor(hex1, hex3)
        res_hex14 = self.xor(hex1, hex4)

        res_hex23 = self.xor(hex2, hex3)
        res_hex24 = self.xor(hex2, hex4)

        res_hex34 = self.xor(hex3, hex4)

        # decriptato a diversi step
        # 1. prima si cercano gli spazi. Si riconoscono perché, se c'è uno spazio su un cipher ed un carattere
        #   su un altro cipher, avrò i primi 2 bit a 01 (tutti i caratteri iniziano con 00, mentre lo spazio con 01)
        # 2. si cerca di capire a quale cipher corrisponde lo spazio (facendo c1 ^ c2, non si può sapere se lo spazio
        #    è di c1 o di c2)
        # 3. si confrontano tutti i cipher per avere quante più informazioni possibili
        # 4. si fa un XOR con i cipher originali per iniziare a scoprire k (facendo c1 ^ p1 si ottiene k)
        #    questo passaggio è lungo e complesso perché bisogna trovare diverse verifiche
        # 5. si avrà una chiave parziale ed un testo parziale e si può iniziare a comprendere il messaggio
        #    inizialmente si vedeva This mess e si capia che voleva dire message
        #    poi compare dec***t che stava per decrypt e via così
        #    basta fare un xor tra l'esadecimale che era presente ed il carattere che si voleva ottenere
        #    così si otteneva k

        # un altro approccio (fallito), era provare ad usare parole comuni e shiftare gli esadecimali
        # fino ad ottenere un testo comprensibile. Ma non riusciva per via delle maiuscole

        print("\n")

        dict12 = self.check_spaces(res_hex12)
        self.test_word_by_position(dict12, hex1, True)
        self.test_word_by_position(dict12, hex2, True)
        print("\n")

        dict13 = self.check_spaces(res_hex13)
        self.test_word_by_position(dict13, hex1, True)
        self.test_word_by_position(dict13, hex3, True)
        print("\n")

        dict14 = self.check_spaces(res_hex14)
        self.test_word_by_position(dict14, hex1, True)
        self.test_word_by_position(dict14, hex4, True)
        print("\n")

        dict23 = self.check_spaces(res_hex23)
        self.test_word_by_position(dict23, hex2, True)
        self.test_word_by_position(dict23, hex3, True)
        print("\n")

        dict24 = self.check_spaces(res_hex24)
        self.test_word_by_position(dict24, hex2, True)
        self.test_word_by_position(dict24, hex4, True)
        print("\n")

        dict34 = self.check_spaces(res_hex34)
        self.test_word_by_position(dict34, hex3, True)
        self.test_word_by_position(dict34, hex4, True)
        print("\n")

        dict_k = {
            0:  'G', # V
            1:  'o', # V
            2:  'o', # V
            3:  'd', # V
            4:  ' ', # V
            5:  't',
            6:  'h',
            7:  'i', # V
            8:  'n',
            9:  'g', # V
            10: 's', # V
            11: ' ',
            12: 'c', # V
            13: 'o',
            14: 'm',
            15: 'e',
            16: ' ', # V
            17: 't', # V
            18: 'o', # oppure tilde
            19: ' ', # V
            20: 't', # V
            21: 'h',
            22: 'o', # V
            23: 's', # V
            24: 'e',  # V
            25: ' ', # V
            26: 'w',
            27: 'h', # V
            28: 'o', # V
            29: ' ',
            30: 'w',
            31: 'a',
            32: 'i',
            33: 't'
        }

        res_k = ""
        for i in range(0, 34):
            if i in dict_k:
                res_k += Color.GREEN + dict_k[i] + Color.RESET
            else:
                res_k += "_"

        # print("".join(v for v in dict_k.values()))
        print(f"Key: {res_k}\n")

        print(self.test_word_by_position(dict_k, self.c1, False))
        print(self.test_word_by_position(dict_k, self.c2, False))
        print(self.test_word_by_position(dict_k, self.c3, False))
        print(self.test_word_by_position(dict_k, self.c4, False))

        """print(res_hex12)
        hex_list = [res_hex12[i:i + 2] for i in range(0, len(res_hex12), 2)]
        binary_list = [bin(int(h, 16))[2:].zfill(8) for h in hex_list]

        dict = {}
        idx = 0

        for binary in binary_list:
            first_2_bit = binary[0:2]
            if first_2_bit == "01":
                dict[idx] = ' '
            idx += 1

        print(dict)

        # print(" ".join(bin(int(h, 16))[2:].zfill(8) for h in hex_list ))

        res = self.test_word_by_position(dict, res_hex12)
        print(res)"""

        # print(' '.join(bin(int(h, 16))[2:].zfill(8) for h in res_hex12))
        # print(f"res: {res_hex}")

        # c = [chr(ord(a) ^ ord(b)) for a, b in zip(hex1, hex2)]

        """res_test = "3c0d094c1f523808000d09"
        word_test = "the"
        word_test = "Hello"
        self.test_word(word_test, res_test)"""

        guess_word = "THE"

        # self.test_word(guess_word, res_hex12)
        # print("\nTest res_hex34")
        # self.test_word(guess_word, res_hex34)

        """print("Test res_hex12")
        self.test_word("THE ", res_hex12)
        print("\nTest res_hex13")
        self.test_word("THE ", res_hex13)
        print("\nTest res_hex14")
        self.test_word("THE ", res_hex14)"""

    def check_spaces(self, hex):
        hex_list = [hex[i:i + 2] for i in range(0, len(hex), 2)]
        binary_list = [bin(int(h, 16))[2:].zfill(8) for h in hex_list]

        dict = {}
        idx = 0

        for binary in binary_list:
            first_2_bit = binary[0:2]
            if first_2_bit == "01":
                dict[idx] = ' '
            idx += 1

        # res = self.test_word_by_position(dict, hex)
        # print(res)
        return dict
        # res = self.test_word_by_position(dict, hex)
        # print(res)

    def test_word_by_position(self, dict, hex, check_print):
        dict_res = {}
        hex_list = [hex[i:i + 2] for i in range(0, len(hex), 2)]
        idx = 0
        res = ""
        for h in hex_list:
            if idx in dict:
                word = dict[idx]
                hex_word = self.ascii_to_hex(word)
                hex_new = self.xor_new(h, hex_word)
                word_new = self.hex_to_ascii(hex_new)
                res += Color.GREEN + word_new + Color.RESET
                dict_res[idx] = word_new
            else:
                res += h
            idx += 1

        if check_print:
            print(res)
            print(dict_res)
        return res

    def test_word(self, word, hex):
        hex_word = self.ascii_to_hex(word)
        hex_len = len(hex_word)
        n = len(hex) - len(hex_word)

        # a = self.xor_new(hex, hex_word)
        # print(self.hex_to_ascii(a))
        # print(a)
        for i in range(0, n):
            hex_test = hex[i:i+hex_len]
            res = self.xor_new(hex_test, hex_word)
            res_ascii = self.hex_to_ascii(res)
            print(f"res: {res},\tascii {res_ascii}")


    def xor_strings(self, xs, ys):
        return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(xs, ys))

    def xor_new(self, hex1, hex2):
        n = 2
        array1 = [hex1[i:i + n] for i in range(0, len(hex1), n)]
        array2 = [hex2[i:i + n] for i in range(0, len(hex2), n)]
        return "".join(hex(int(x, 16) ^ int(y, 16))[2:].zfill(2) for x, y in zip(array1, array2))

    def xor(self, phrase1, phrase2):
        # print(f"phrase1 : {phrase1}")
        # print(f"phrase2 :e {phrase2}")

        b1 = self.hex_to_binary(phrase1)
        b2 = self.hex_to_binary(phrase2)

        # print(f"b1 : {b1}")
        # print(f"b2 : {b2}")

        xor_result = ""
        for i in range(0, len(b1)):
            int1 = int(b1[i])
            int2 = int(b2[i])
            xor_result += str(int1 ^ int2)

        # print(f"xor: {xor_result}")
        return self.binary_to_hex(xor_result)
        # ascii_result = self.binary_to_ascii(xor_result)
        # return ascii_result

    def binary_to_hex(self, binary):
        n = 4

        binary_list = [binary[i:i + n] for i in range(0, len(binary), n)]
        return "".join(hex(int(b, 2))[2:] for b in binary_list)

        """
        scale = 2  # equals to hexadecimal
        num_of_bits = 2
        
        hex_result = ""
        
        for binary in binary_list:
            binary_value = hex(int(binary, scale))[2:].zfill(num_of_bits)
            hex_result += binary_value
        return hex_result"""

    def hex_to_binary(self, hexdata):
        num_of_bits = 4
        return ''.join(bin(int(h, 16))[2:].zfill(num_of_bits) for h in hexdata)

        """
        # https://www.overcoded.net/python-convert-hexadecimal-to-binary-111821/
        scale = 16  # equals to hexadecimal
        num_of_bits = 8
        # a = bin(int(hexdata, scale))
        n = 2
        hex_result = ""
        hex_list = [hexdata[i:i + n] for i in range(0, len(hexdata), n)]
        for hex in hex_list:
            binary_value = bin(int(hex, scale))[2:].zfill(num_of_bits)
            hex_result += binary_value
        return hex_result
        """
        # return bin(int(hexdata, scale))[2:].zfill(num_of_bits)

    def binary_to_ascii(self, binary):
        scale = 2
        # x = chr(int(binary, scale))

        ascii_result = ""
        n = 8
        binary_list = [binary[i:i + n] for i in range(0, len(binary), n)]
        for binary in binary_list:
            ascii = chr(int(binary, scale))
            ascii_result += ascii

        # return ascii_result
        return binary_list

    def ascii_to_hex(self, ascii):
        return ascii.encode("ascii").hex()

    def hex_to_ascii(self, hex):
        n = 2
        hex_list = [hex[i:i + n] for i in range(0, len(hex), n)]
        return "".join(chr(int(h, 16)) for h in hex_list)
    
"""
1d -> r
14 -> y
15 -> p

06 -> n
16 -> w
49 -> i

01001001
01101001
00100000




00010110
01110111
01100001



00000110
01101110
01101000



00010101
01110000
01100101



00010100
01111001
01101101



00011101
01110010
01101111
"""
