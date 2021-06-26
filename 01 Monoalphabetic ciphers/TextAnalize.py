from Alphabet import Alphabet


class TextAnalize:
    def __init__(self, text):
        self.text = text

    def analyze(self):
        dict = {}
        for c in Alphabet.CHARACTERS:
            dict[c] = 0

        for char in self.text:
            if char in Alphabet.CHARACTERS:
                dict[char] += 1
        dict = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1], reverse=False)}

        for key in dict:
            value = dict[key]
            print(f"Key {key} : {value}")

        return dict
        #print(dict)
