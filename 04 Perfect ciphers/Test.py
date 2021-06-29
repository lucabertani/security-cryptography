from Color import Color


class Test:

    # prova per capire se gli algoritmi di hex, ascii, xor funzionano
    def test(self):
        """a = "CIAO MONDOO"
        b = "HELLO WORLD"
        k = "AJEJEPRAZOR"""

        a = "A "
        b = " B"
        k = "AA"

        hex_a = self.ascii_to_hex(a)
        hex_b = self.ascii_to_hex(b)
        hex_k = self.ascii_to_hex(k)

        xor_a_k = self.xor_new(hex_a, hex_k)
        xor_b_k = self.xor_new(hex_b, hex_k)
        xor_a_b = self.xor_new(xor_a_k, xor_b_k)

        # print(f"Hex a:   {hex_a}")
        # print(f"Hex b:   {hex_b}")
                                               # 0b0c0d036f6d180116030b
        # xor_a_b = self.xor_new(hex_a, hex_b) # 0b0c0d036f6d180116030b
        print(f"xor_a_b: {xor_a_b}")

        print(f"xor_a_k: {self.hex_to_binary(xor_a_k)}")
        print(f"xor_a_k: {self.hex_to_binary(xor_a_b)}")

        dict = self.check_spaces(xor_a_b)
        res = self.test_word_by_position(dict, xor_a_b)
        print(res)

        print(self.test_word_by_position(dict, xor_a_k))
        print(self.test_word_by_position(dict, xor_b_k))

    def ascii_to_hex(self, ascii):
        return ascii.encode("ascii").hex()

    def xor_new(self, hex1, hex2):
        n = 2
        array1 = [hex1[i:i + n] for i in range(0, len(hex1), n)]
        array2 = [hex2[i:i + n] for i in range(0, len(hex2), n)]
        return "".join(hex(int(x, 16) ^ int(y, 16))[2:].zfill(2) for x, y in zip(array1, array2))

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

        return dict
        # res = self.test_word_by_position(dict, hex)
        # print(res)

    def test_word_by_position(self, dict, hex):
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
            else:
                res += h
            idx += 1
        return res

    def hex_to_ascii(self, hex):
        n = 2
        hex_list = [hex[i:i + n] for i in range(0, len(hex), n)]
        return "".join(chr(int(h, 16)) for h in hex_list)

    def hex_to_binary(self, hexdata):
        num_of_bits = 4
        return ''.join(bin(int(h, 16))[2:].zfill(num_of_bits) for h in hexdata)