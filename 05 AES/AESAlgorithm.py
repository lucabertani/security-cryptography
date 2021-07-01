class AESAlgorithm:
    sbox = [99, 124, 119, 123, 242, 107, 111, 197, 48, 1, 103, 43, 254, 215, 171, 118, 202, 130, 201, 125, 250, 89, 71,
            240, 173, 212, 162, 175, 156, 164, 114, 192, 183, 253, 147, 38, 54, 63, 247, 204, 52, 165, 229, 241, 113,
            216, 49, 21, 4, 199, 35, 195, 24, 150, 5, 154, 7, 18, 128, 226, 235, 39, 178, 117, 9, 131, 44, 26, 27, 110,
            90, 160, 82, 59, 214, 179, 41, 227, 47, 132, 83, 209, 0, 237, 32, 252, 177, 91, 106, 203, 190, 57, 74, 76,
            88, 207, 208, 239, 170, 251, 67, 77, 51, 133, 69, 249, 2, 127, 80, 60, 159, 168, 81, 163, 64, 143, 146, 157,
            56, 245, 188, 182, 218, 33, 16, 255, 243, 210, 205, 12, 19, 236, 95, 151, 68, 23, 196, 167, 126, 61, 100,
            93, 25, 115, 96, 129, 79, 220, 34, 42, 144, 136, 70, 238, 184, 20, 222, 94, 11, 219, 224, 50, 58, 10, 73, 6,
            36, 92, 194, 211, 172, 98, 145, 149, 228, 121, 231, 200, 55, 109, 141, 213, 78, 169, 108, 86, 244, 234, 101,
            122, 174, 8, 186, 120, 37, 46, 28, 166, 180, 198, 232, 221, 116, 31, 75, 189, 139, 138, 112, 62, 181, 102,
            72, 3, 246, 14, 97, 53, 87, 185, 134, 193, 29, 158, 225, 248, 152, 17, 105, 217, 142, 148, 155, 30, 135,
            233, 206, 85, 40, 223, 140, 161, 137, 13, 191, 230, 66, 104, 65, 153, 45, 15, 176, 84, 187, 22]

    isbox = [82, 9, 106, 213, 48, 54, 165, 56, 191, 64, 163, 158, 129, 243, 215, 251, 124, 227, 57, 130, 155, 47, 255,
             135, 52, 142, 67, 68, 196, 222, 233, 203, 84, 123, 148, 50, 166, 194, 35, 61, 238, 76, 149, 11, 66, 250,
             195, 78, 8, 46, 161, 102, 40, 217, 36, 178, 118, 91, 162, 73, 109, 139, 209, 37, 114, 248, 246, 100, 134,
             104, 152, 22, 212, 164, 92, 204, 93, 101, 182, 146, 108, 112, 72, 80, 253, 237, 185, 218, 94, 21, 70, 87,
             167, 141, 157, 132, 144, 216, 171, 0, 140, 188, 211, 10, 247, 228, 88, 5, 184, 179, 69, 6, 208, 44, 30,
             143, 202, 63, 15, 2, 193, 175, 189, 3, 1, 19, 138, 107, 58, 145, 17, 65, 79, 103, 220, 234, 151, 242, 207,
             206, 240, 180, 230, 115, 150, 172, 116, 34, 231, 173, 53, 133, 226, 249, 55, 232, 28, 117, 223, 110, 71,
             241, 26, 113, 29, 41, 197, 137, 111, 183, 98, 14, 170, 24, 190, 27, 252, 86, 62, 75, 198, 210, 121, 32,
             154, 219, 192, 254, 120, 205, 90, 244, 31, 221, 168, 51, 136, 7, 199, 49, 177, 18, 16, 89, 39, 128, 236,
             95, 96, 81, 127, 169, 25, 181, 74, 13, 45, 229, 122, 159, 147, 201, 156, 239, 160, 224, 59, 77, 174, 42,
             245, 176, 200, 235, 187, 60, 131, 83, 153, 97, 23, 43, 4, 126, 186, 119, 214, 38, 225, 105, 20, 99, 85, 33,
             12, 125]

    rcon = [141, 1, 2, 4, 8]

    def __init__(self, key, plain_text):
        self.key = []
        self.state = []

        key_list = [key[i:i + 2] for i in range(0, len(key), 2)]
        for h in key_list:
            self.key.append(int(h, 16))

        plain_text_list = [plain_text[i:i + 2] for i in range(0, len(plain_text), 2)]
        for h in plain_text_list:
            self.state.append(int(h, 16))

        self.print_hex("key", self.key)
        self.print_hex("plain_text", self.state)

        self.Nb = 4
        self.Nk = int(len(self.key) / self.Nb)
        self.Nr = self.Nb + 6

        self.w = []

        print(f"Nb: {self.Nb}, Nk: {self.Nk}, Nr: {self.Nr}")


    # def AddRoundKey(self):

    def encrypt(self):
        self.KeyExpansion(0, self.Nb-1)
        self.state = self.xor_list(self.state, self.w)
        self.print_hex("Start", self.state)
        self.state = self.SubBytes(self.state)
        self.print_hex("SubBytes", self.state)


    def KeyExpansion(self, start, end):
        w = self.w
        Nk = self.Nk
        i = start

        while i < self.Nk and i <= end:
            w.append(self.key[4 * i])
            w.append(self.key[4 * i+1])
            w.append(self.key[4 * i+2])
            w.append(self.key[4 * i+3])
            i += 1

        i = Nk
        while i <= end:
            temp = [w[i-4], w[i-3], w[i-2], w[i-1]]
            if i % Nk == 0:
                temp = self.xor_list(
                    self.SubWord(self.RotWord(temp)),
                    self.Rcon(int(i / Nk))
                )
            elif Nk > 6 and i % Nk == 4:
                temp = self.SubWord(temp)

            r = self.xor_list(w[i-Nk:i-Nk+4], temp)
            w.append(r[0])
            w.append(r[1])
            w.append(r[2])
            w.append(r[3])
            i += 1

        # self.print_hex(w)

    def RotWord(self, hex_list):
        l = hex_list.copy()
        t = l[0]
        l.pop(0)
        l.append(t)
        return l

    def SubWord(self, hex_list):
        r = []
        for h in hex_list:
            s = self.sbox[h]
            r.append(s)
        return r

    def SubBytes(self, hex_array):
        r = []
        for h in hex_array:
            s = self.sbox[h]
            r.append(s)
        return r

    def Rcon(self, idx):
        r = []
        r.append(self.rcon[idx])
        r.append(0)
        r.append(0)
        r.append(0)
        return r

    def xor_list(self, l1, l2):
        r = []
        for x,y in zip(l1,l2):
            r.append(x ^ y)
        return r

    def print_hex(self, msg, hex_array):
        s = "".join(hex(h)[2:].zfill(2) for h in hex_array)
        print(f"{msg}: {s}")
"""
while (i < Nb * (Nr+1)]
    temp = w[i-1]
    if (i mod Nk = 0)
        temp = SubWord(RotWord(temp)) xor Rcon[i/Nk]
    else if (Nk > 6 and i mod Nk = 4)
        temp = SubWord(temp)
    end if
    w[i] = w[i-Nk] xor temp
    i = i + 1
end while
"""


"""
while (i < Nk)
    w[i] = word(key[4*i], key[4*i+1], key[4*i+2], key[4*i+3])
    i = i+1
end while
"""


"""
AddRoundKey(state, w[0, 3])

for round in range(1,Nr):
    SubBytes(state)
    ShiftRows(state)
    MixColumns(state)
    AddRoundKey(state, w[round*4, round*4+3])

SubBytes(state)
ShiftRows(state)
AddRoundKey(state, w[Nr*4, Nr*4+3])
"""

