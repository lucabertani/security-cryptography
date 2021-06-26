class Alphabet:
    CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    SIZE = len(CHARACTERS)

    # https://en.wikipedia.org/wiki/Letter_frequency
    # https://www.thefreedictionary.com/words-that-end-in-ost
    WORD_USAGE = {
        "A": 0.082,
        "B": 0.015,
        "C": 0.028,
        "D": 0.043,
        "E": 0.13,
        "F": 0.022,
        "G": 0.02,
        "H": 0.061,
        "I": 0.07,
        "J": 0.0015,
        "K": 0.0077,
        "L": 0.04,
        "M": 0.024,
        "N": 0.067,
        "O": 0.075,
        "P": 0.019,
        "Q": 0.00095,
        "R": 0.06,
        "S": 0.063,
        "T": 0.091,
        "U": 0.028,
        "V": 0.0098,
        "W": 0.024,
        "X": 0.0015,
        "Y": 0.02,
        "Z": 0.00074
    }

    WORD_USAGE_SORT_ASC = {k: v for k, v in sorted(WORD_USAGE.items(), key=lambda item: item[1], reverse=True)}