class PerfectAlphabetic:
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

    def test(self):
        """
        s1 = "A" # 01000001
        s2 = "Z" # 01000010 per B
                 # 01011010 per Z
                 # 01000000 per spazio
                 # 01100001 per a
                 # 01111010 per z
                 # 00010001
        # c = [chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2)]
        c = [ord(a) ^ ord(b) for a, b in zip(s1, s2)]
        print(f"c: {c}")
        d = ' '.join(format(ord(x), 'b') for x in s1)
        e = ' '.join(format(ord(x), 'b') for x in s2)
        print(f"d: {d}")
        print(f"e: {e}")
        """


    def crack_cipher(self):
        """
        b1 = self.hex_to_binary(self.c1)
        b2 = self.hex_to_binary(self.c2)
        print(f"b1:  {b1}")
        print(f"b2:  {b2}")

        # print(f"b1[0] = {b1[0]}, b2[0] = {b2[0]}")


        b12 = ""
        for i in range(0, len(b1)):
            char1 = int(b1[i])
            char2 = int(b2[i])
            b12 += str(char1 ^ char2)
            # print(f"char1 = {char1}, char2 = {char2}")

        print(f"xor: {b12}")
        ascii12 = self.binary_to_ascii(b12)
        print(f"ascii12: {ascii12}")

        # b12 = b1[0] ^ b2[0]
        # b12 = b1 ^ b2
        """

        hex_test = "6369616f6d6f6e646f"
        bin_test = self.hex_to_binary(hex_test)
        ascii_test = self.binary_to_ascii(bin_test)
        print(f"Ascii_test: {ascii_test}")

        b1 = self.hex_to_binary(self.c1)
        b2 = self.hex_to_binary(self.c2)
        b3 = self.hex_to_binary(self.c3)
        b4 = self.hex_to_binary(self.c4)

        b12 = self.xor(b1, b2)
        b13 = self.xor(b1, b3)
        b14 = self.xor(b1, b4)
        print(f"ascii12: {b12}")
        print(f"ascii13: {b13}")
        print(f"ascii14: {b14}")

        b21 = self.xor(b2, b1)
        b23 = self.xor(b2, b3)
        b24 = self.xor(b2, b4)
        print(f"ascii21: {b21}")
        print(f"ascii23: {b23}")
        print(f"ascii24: {b24}")

        b31 = self.xor(b3, b1)
        b32 = self.xor(b3, b2)
        b34 = self.xor(b3, b4)
        print(f"ascii31: {b31}")
        print(f"ascii32: {b32}")
        print(f"ascii34: {b34}")

        b41 = self.xor(b4, b1)
        b42 = self.xor(b4, b2)
        b43 = self.xor(b4, b3)
        print(f"ascii41: {b41}")
        print(f"ascii42: {b42}")
        print(f"ascii43: {b43}")

    def xor(self, phrase1, phrase2):
        b1 = self.hex_to_binary(phrase1)
        b2 = self.hex_to_binary(phrase2)

        print(f"b1 : {b1}")
        print(f"b2 : {b2}")

        xor_result = ""
        for i in range(0, len(b1)):
            char1 = int(b1[i])
            char2 = int(b2[i])
            xor_result += str(char1 ^ char2)

        print(f"xor: {xor_result}")
        ascii_result = self.binary_to_ascii(xor_result)
        return ascii_result


    def hex_to_binary(self, hexdata):
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



