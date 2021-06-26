"""
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
"""
from Alphabet import Alphabet
from Color import Color
from MonoAlphabetic import MonoAlphabetic

if __name__ == '__main__':
    mono_alphabetic = MonoAlphabetic("resources/cipher.txt")
    mono_alphabetic.analize()
    #print(f"{Color.GREEN}testo di prova{Color.RESET}")

    #mono_alphabetic.replace_by_usage()

    mono_alphabetic.add_replace("C", "O")
    mono_alphabetic.add_replace("K", "E")
    mono_alphabetic.add_replace("A", "R")
    mono_alphabetic.add_replace("O", "S")
    mono_alphabetic.add_replace("W", "N")
    mono_alphabetic.add_replace("L", "A")
    mono_alphabetic.add_replace("B", "D")
    mono_alphabetic.add_replace("D", "I")
    mono_alphabetic.add_replace("G", "T")
    mono_alphabetic.add_replace("N", "H")
    mono_alphabetic.add_replace("F", "P")
    mono_alphabetic.add_replace("Y", "L")
    mono_alphabetic.add_replace("S", "U")
    mono_alphabetic.add_replace("X", "W")
    mono_alphabetic.add_replace("Z", "Y")
    mono_alphabetic.add_replace("I", "R")
    mono_alphabetic.add_replace("R", "X")
    mono_alphabetic.add_replace("Q", "G")
    mono_alphabetic.add_replace("H", "C")
    mono_alphabetic.add_replace("E", "M")
    mono_alphabetic.add_replace("J", "V")
    mono_alphabetic.add_replace("M", "K")

    mono_alphabetic.decrypt()

    mono_alphabetic.print_key()
    #print(Alphabet.WORD_USAGE_SORT_ASC)
