from AESAlgorithm import process_key, SubBytes, ShiftRows, print_hex, InvShiftRows, InvSubBytes, MixColumns,\
    InvMixColumns, AddRoundKey, KeyExpansionInv, sbox, isbox, print_binary, print_ascii
from Color import Color


class AESCrack:
    def __init__(self, cipher_path):
        self.cipher_path = cipher_path

        f = open(cipher_path, "r")
        self.cipher = f.read()
        f.close()

        # print(self.cipher)

        self.c1, self.c2, self.c3, self.c4,\
            self.c5, self.c6, self.c7, self.c8,\
            self.c9 = self.cipher.split('\n')

        # print(self.c1)
        # print(self.c2)
        # print(self.c3)
        # print(self.c4)
        # print(self.c5)
        # print(self.c6)
        # print(self.c7)
        # print(self.c8)
        # print(self.c9)
        # print("")

    def find_spaces(self, c1, c2):
        space = " "
        space_hex = int(space.encode().hex(), 16)
        space_hex_s = sbox[space_hex]

        state1 = InvSubBytes(InvShiftRows(c1))
        state2 = InvSubBytes(InvShiftRows(c2))
        # k_mix = SubBytes(ShiftRows(k))
        state1_m = InvShiftRows(InvMixColumns(state1))
        state2_m = InvShiftRows(InvMixColumns(state2))
        res_hex12 = AddRoundKey(state1_m, state2_m)  # rimuovo k!
        # res_hex12 = AddRoundKey(state1, state2) # rimuovo k!
        # res_hex12 = InvShiftRows(InvMixColumns(res_hex12)) # rimetto nell'ordine corretto, quindi ottengo sbox[plain1] XOR sbox[plain2]


        """k = [
            [0x00, space_hex_s, 0x00, 0x00],
            [0x00, 0x00, 0x00, 0x00],
            [0x00, 0x00, 0x00, 0x00],
            [0x00, 0x00, 0x00, 0x00]
        ]"""
        k = [
            [space_hex, space_hex, space_hex, space_hex],
            [space_hex, space_hex, space_hex, space_hex],
            [0x00, 0x00, 0x00, 0x00],
            [0x00, 0x00, 0x00, 0x00]
        ]
        print_hex("k", k)
        res_k = state1
        res_k = InvShiftRows(InvMixColumns(res_k))
        print_hex("res_k", res_k)
        res_k = AddRoundKey(res_k, k) # plain1 XOR k
        print_hex("AddRoundKey", res_k)
        res_k = InvSubBytes(res_k)
        print_hex("InvSubBytes", res_k)


        # print_hex("res_hex12", res_hex12)
        print_binary("res_hex12", res_hex12)

        space = " "
        space_hex = int(space.encode().hex(), 16)
        space_hex_s = sbox[space_hex]
        # space_binary = bin(space_hex)[2:].zfill(8)
        # space_binary_s = bin(space_hex_s)[2:].zfill(8)

        res_xor12_s = [[None for j in range(4)] for i in range(4)]

        for i, word in enumerate(res_hex12):
            for j, byte in enumerate(word):
                res_xor12_s[i][j] = byte ^ space_hex_s

        print_binary("res_xor12_s", res_xor12_s)
        final_s = InvSubBytes(res_xor12_s)
        print_binary("final_s", final_s)


        dict = {}
        idx = 0
        for word in final_s:
            for byte in word:
                # if byte >= 0x20 and byte <= 0x7A:
                if byte == 0x20 or (byte >= 0x41 and byte <= 0x5A) or (byte >= 0x61 and byte <= 0x7A):
                    # ho un carattere ascii valido!
                    dict[idx] = chr(byte)
                idx += 1

        # print(dict)
        return dict

    def find_all_spaces(self):
        list = [process_key(self.c1), process_key(self.c2), process_key(self.c3), process_key(self.c4),
                process_key(self.c5), process_key(self.c6), process_key(self.c7), process_key(self.c8),
                process_key(self.c9)]
        dict_spaces = {}
        for i in range(16):
            dict_spaces[i] = 0

        for i in range(9):
            for j in range(i+1, 9):
                # print(f"i: {i}, j: {j}")
                c1 = list[i]
                c2 = list[j]
                dict = self.find_spaces(c1, c2)
                for key in dict:
                    dict_spaces[key] += 1

        print(dict_spaces)


    def test(self):
        # t1 = "HELLO NEW WORLD!"
        # t2 = "YOU'RE WELCOMEEE"
        # t2 = "HELLOONEW WORLD!"
        # t1 = "A AAAAAAAAAAAAAA"
        # t2 = "AR RRRRRRRRRRRRR"
        # t1 = "AAAAAAAAAAAAAAAC"
        # t2 = "ABCDEFGHILMNOPQ "
        t1 = "ABCDEFGHIJKLMNOP"
        t2 = "W               "
        # plain_key = "000102030405060708090a0b0c0d0e0f"
        plain_key = "000102030405060708090a0b0c0d0e0f"
        h1 = self.ascii_to_hex(t1)
        h2 = self.ascii_to_hex(t2)

        k = process_key(plain_key)
        h1 = process_key(h1)
        h2 = process_key(h2)

        c1 = self.test_cipher(h1, k)
        c2 = self.test_cipher(h2, k)

        # print_hex("h1", h1)
        print("decrypt", self.state_to_ascii(self.test_decrypt(c1, k)))

        a = self.find_spaces(c1, c2)
        print(a)
        # self.find_all_spaces()

        """
        
        # c1 = InvMixColumns(InvShiftRows(InvSubBytes(c1)))
        # c2 = InvMixColumns(InvShiftRows(InvSubBytes(c2)))

        c1 = InvSubBytes(InvShiftRows(c1))
        c2 = InvSubBytes(InvShiftRows(c2))

        # c1 ^ k - c2 ^ k
        # c1^c2 !!
        
        

        
        res_hex12 = AddRoundKey(c1, c2)
        print_hex("res_hex12", res_hex12)
        # res_hex12 = InvSubBytes(InvShiftRows(InvMixColumns(res_hex12)))
        res_hex12 = InvShiftRows(InvMixColumns(res_hex12))
        print_hex("res_hex12", res_hex12)
        print_binary("res_hex12", res_hex12)
        # quando 2 caratteri combaciano, esce il valore esadecimale 52 (ovvero R in ascii)

        space = " "
        space_hex = int(space.encode().hex(), 16)
        space_binary = bin(space_hex)[2:].zfill(8)
        print(space_binary)

        space_hex_s = sbox[space_hex]
        space_binary_s = bin(space_hex_s)[2:].zfill(8)
        print(space_binary_s)

        res_xor12_s = [[None for j in range(4)] for i in range(4)]

        for i, word in enumerate(res_hex12):
            for j, byte in enumerate(word):
                res_xor12_s[i][j] = byte ^ space_hex_s

        final_s = InvSubBytes(res_xor12_s)
        print_hex("final_s", final_s)
        print("decrypt", self.state_to_ascii(final_s))
        """


        """
        print("decrypt", self.state_to_ascii(res_hex12))

        print("\n")

        dict12 = self.check_spaces(res_hex12)
        self.test_word_by_position(dict12, c1, True)
        self.test_word_by_position(dict12, c2, True)
        print("\n")
        """

    def test_cipher(self, block, k):
        state = block
        state = SubBytes(state)
        state = ShiftRows(state)
        state = MixColumns(state)
        state = AddRoundKey(state, k)
        state = SubBytes(state)
        state = ShiftRows(state)
        return state

    def test_decrypt(self, block, k):
        state = block
        state = InvShiftRows(state)
        state = InvSubBytes(state)
        state = AddRoundKey(state, k)
        state = InvMixColumns(state)
        # state = InvMixColumns(state)
        # state = AddRoundKey(state, InvMixColumns(k))
        state = InvShiftRows(state)
        state = InvSubBytes(state)
        return state


    def crack(self):
        """
        plain_text = "00112233445566778899aabbccddeeff"
        plain_key = "000102030405060708090a0b0c0d0e0f"
        t = process_key(plain_text)
        k = process_key(plain_key)

        state = t

        print_hex("Start:", state)

        state = SubBytes(state)
        print_hex("SubBytes:", state)

        state = ShiftRows(state)
        print_hex("ShiftRows:", state)

        state = MixColumns(state)
        print_hex("MixColumns:", state)

        state = AddRoundKey(state, k)
        print_hex("AddRoundKey:", state)

        state = SubBytes(state)
        print_hex("SubBytes:", state)

        state = ShiftRows(state)
        print_hex("ShiftRows:", state)

        # state = InvShiftRows(state)
        # state = InvSubBytes(state)
        # state = AddRoundKey(state, k)
        # state = InvMixColumns(state)
        # state = InvShiftRows(state)
        # state = InvSubBytes(state)

        state = InvShiftRows(state)
        state = InvSubBytes(state)
        state = InvMixColumns(state)
        state = AddRoundKey(state, InvMixColumns(k))
        state = InvShiftRows(state)
        state = InvSubBytes(state)

        print_hex("AddRoundKey:", state)
        """


        """
        k1 = SubBytes(k)
        k2 = ShiftRows(k1)

        print_hex("k2", k2)

        inv_k = InvShiftRows(InvSubBytes(k2))
        print_hex("inv_k", inv_k)
        """

        # c1 = process_key(self.c1)
        # c1 = InvMixColumns(InvShiftRows(InvSubBytes(c1)))
        c1 = InvMixColumns(InvShiftRows(InvSubBytes(process_key(self.c1))))
        c2 = InvMixColumns(InvShiftRows(InvSubBytes(process_key(self.c2))))
        c3 = InvMixColumns(InvShiftRows(InvSubBytes(process_key(self.c3))))
        c4 = InvMixColumns(InvShiftRows(InvSubBytes(process_key(self.c4))))
        c5 = InvMixColumns(InvShiftRows(InvSubBytes(process_key(self.c5))))
        c6 = InvMixColumns(InvShiftRows(InvSubBytes(process_key(self.c6))))
        c7 = InvMixColumns(InvShiftRows(InvSubBytes(process_key(self.c7))))
        c8 = InvMixColumns(InvShiftRows(InvSubBytes(process_key(self.c8))))
        c9 = InvMixColumns(InvShiftRows(InvSubBytes(process_key(self.c9))))

        # print_hex("c1", c1)
        # print_hex("c2", c2)
        # print_hex("c3", c3)
        # print_hex("c4", c4)
        # print_hex("c5", c5)
        # print_hex("c6", c6)
        # print_hex("c7", c7)
        # print_hex("c8", c8)
        # print_hex("c9", c9)

        res_hex12 = AddRoundKey(c1, c2)
        res_hex12 = InvSubBytes(InvShiftRows(res_hex12))
        print_hex("res_hex12", res_hex12)

        print("\n")

        dict12 = self.check_spaces(res_hex12)
        self.test_word_by_position(dict12, c1, True)
        self.test_word_by_position(dict12, c2, True)
        print("\n")

    def check_spaces(self, state):
        hex_str = ""
        for word in state:
            for byte in word:
                hex_str += (hex(byte)[2:].zfill(2))

        hex_list = [hex_str[i:i + 2] for i in range(0, len(hex_str), 2)]
        binary_list = [bin(int(h, 16))[2:].zfill(8) for h in hex_list]

        dict = {}
        idx = 0

        for binary in binary_list:
            first_2_bit = binary[0:2]
            if first_2_bit == "01":
                dict[idx] = ' '
            idx += 1

        return dict

    def test_word_by_position(self, dict, state, check_print):
        idx = 0
        Nb = len(state)
        new_state = [[None for j in range(4)] for i in range(Nb)]

        for i, word in enumerate(state):
            for j, byte in enumerate(word):
                if idx in dict:
                    word = dict[idx]
                    hex_word = self.ascii_to_hex(word)
                    new_state[i][j] = byte ^ int(hex_word, 16)
                else:
                    new_state[i][j] = byte
                idx += 1

        new_state = InvSubBytes(InvShiftRows(new_state))

        dict_res = {}
        s = ""
        idx = 0
        for word in state:
            for byte in word:
                # h = hex(byte)[2:].zfill(2)
                h = chr(byte)
                if idx in dict:
                    dict_res[idx] = h
                    h = Color.GREEN + h + Color.RESET
                s += h
                idx += 1

        if check_print:
            print(s)
            print(dict_res)

        return new_state

        """
        hex_str = ""
        for word in state:
            for byte in word:
                hex_str += (hex(byte)[2:].zfill(2))

        dict_res = {}
        hex_list = [hex_str[i:i + 2] for i in range(0, len(hex_str), 2)]
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
        """

    def xor_new(self, hex1, hex2):
        n = 2
        array1 = [hex1[i:i + n] for i in range(0, len(hex1), n)]
        array2 = [hex2[i:i + n] for i in range(0, len(hex2), n)]
        return "".join(hex(int(x, 16) ^ int(y, 16))[2:].zfill(2) for x, y in zip(array1, array2))

    def ascii_to_hex(self, ascii):
        return ascii.encode("ascii").hex()

    def hex_to_ascii(self, hex):
        n = 2
        hex_list = [hex[i:i + n] for i in range(0, len(hex), n)]
        return "".join(chr(int(h, 16)) for h in hex_list)

    def state_to_ascii(self, state):
        s = ""
        for word in state:
            for byte in word:
                s += chr(byte)
        return s

