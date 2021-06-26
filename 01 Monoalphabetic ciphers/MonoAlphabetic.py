from Alphabet import Alphabet
from Color import Color
from TextAnalize import TextAnalize


class MonoAlphabetic:
    def __init__(self, cipher_path):
        self.cipher_path = cipher_path

        f = open(cipher_path, "r")
        self.cipher = f.read()
        f.close()

        self.dict_replace = {}
        self.decrypted = ""
        #print(f.read())

    def analize(self):
        text_analyzer = TextAnalize(self.cipher)
        text_analyzer.analyze()

    def replace_by_usage(self):
        text_analyzer = TextAnalize(self.cipher)
        dict = text_analyzer.analyze()
        dict_usage = []
        i = 0

        for key in Alphabet.WORD_USAGE_SORT_ASC:
            dict_usage.append(key)

        for c in dict:
            r = dict_usage[i]
            self.add_replace(c, r)
            i = i + 1

    def add_replace(self, from_character, to_character):
        self.dict_replace[from_character] = to_character

    def decrypt(self):
        self.decrypted = ""

        for c in self.cipher:
            if c in self.dict_replace:
                res = self.dict_replace[c]
                self.decrypted += Color.GREEN + res + Color.RESET
            else:
                self.decrypted += c

        print(f"Encrypted: \n{self.cipher}")
        print(f"Decrypted: \n{self.decrypted}")

    def print_key(self):
        # dict = {k: v for k, v in sorted(self.dict_replace.items(), key=lambda item: item[1], reverse=False)}
        dict_sort = dict(sorted(self.dict_replace.items()))
        alphabet = ""
        key = ""

        for k in dict_sort:
            alphabet += k
            key += dict_sort[k]

        print(f"Alphabet: {alphabet}\nKey     : {key}")