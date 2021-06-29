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

        # ascii_start = "CIAOMONDO"
        # hex_test = ''.join(hex(ord(x))[2:] for x in ascii_start)
        # print(hex_test)

        # bin_test = self.hex_to_binary(hex_test)
        # ascii_test = self.binary_to_ascii(bin_test)
        # print(f"Ascii_test: {ascii_test}")

        """hex1 = self.c1
        hex2 = self.c2
        binary_a = hex1.decode("hex")
        binary_b = hex2.decode("hex")
        xored = self.xor_strings(binary_a, binary_b).encode("hex")
        print(xored)"""

        hex1 = self.c1
        hex2 = self.c2

        # print(self.hex_to_binary("A"))
        # print(self.binary_to_hex("1010"))

        res = self.xor(hex1, hex2)
        print(f"res: {res}")

        # c = [chr(ord(a) ^ ord(b)) for a, b in zip(hex1, hex2)]

    def xor_strings(self, xs, ys):
        return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(xs, ys))


    def xor(self, phrase1, phrase2):
        print(f"phrase1 : {phrase1}")
        print(f"phrase2 : {phrase2}")

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

    

