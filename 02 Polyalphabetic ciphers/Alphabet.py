class Alphabet:
    CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    SIZE = len(CHARACTERS)

    # https://en.wikipedia.org/wiki/Letter_frequency
    # https://github.com/drewp41/Vigenere-Cipher-Breaker/blob/master/Vigenere_cipher.py
    # https://www.thefreedictionary.com/words-that-end-in-ost

    ENGLISH_FREQUENCIES = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015,
                              0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,
                              0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,
                              0.00978, 0.02360, 0.00150, 0.01974, 0.00074]

    WORD_USAGE = {
        "A": 0.08167,
        "B": 0.01492,
        "C": 0.02782,
        "D": 0.04253,
        "E": 0.12702,
        "F": 0.02228,
        "G": 0.02015,
        "H": 0.06094,
        "I": 0.06966,
        "J": 0.00153,
        "K": 0.00772,
        "L": 0.04025,
        "M": 0.02406,
        "N": 0.06749,
        "O": 0.07507,
        "P": 0.01929,
        "Q": 0.00095,
        "R": 0.05987,
        "S": 0.06327,
        "T": 0.09056,
        "U": 0.02758,
        "V": 0.00978,
        "W": 0.02360,
        "X": 0.00150,
        "Y": 0.01974,
        "Z": 0.00074
    }

    WORD_USAGE_SORT_ASC = {k: v for k, v in sorted(WORD_USAGE.items(), key=lambda item: item[1], reverse=True)}