from AESAlgorithm import process_key, SubBytes, ShiftRows, print_hex, InvShiftRows, InvSubBytes, MixColumns,\
    InvMixColumns, AddRoundKey, KeyExpansionInv
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

