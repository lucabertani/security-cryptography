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
from PolyAlphabetic import PolyAlphabetic

if __name__ == '__main__':
    poly_alphabetic = PolyAlphabetic("resources/cipher.txt")
    key_length = poly_alphabetic.get_key_length()
    print(f"Key Length: {key_length}")

    key = poly_alphabetic.get_key(key_length)
    print(f"Key: {key}")

    plain_text = poly_alphabetic.decrypt(key)
    print(f"Plain text: {plain_text}")

    # ALICE WAS BEGINNING TO GET VERY TIRED OF SITTING BY HER SISTER ON THE BANK AND OF HAVING NOTHING TO DO ONCE OR TWICE SHE HAD PEEPED INTO THE BOOK HER SISTER WAS READING BUT IT HAD NO PICTURES OR CONVERSATIONS IN IT AND WHAT IS THE USE OF A BOOK THOUGHT ALICE WITHOUT PICTURES OR CONVERSATION SO SHE WAS CONSIDERING IN HER OWN MIND AS WELL AS SHE COULD FOR THE HOT DAY MADE HER FEEL VERY SLEEPY AND STUPID WHETHER THE PLEASURE OF MAKING A DAISY CHAIN WOULD BE WORTH THE TROUBLE OF GETTING UP AND PICKING THE DAISIES WHEN SUDDENLY A WHITE RABBIT WITH PINK EYES RAN CLOSE BY HER THERE WAS NOTHING SO VERY REMARKABLE IN THAT NOR DID ALICE THINK IT SO VERY MUCH OUT OF THE WAY TO HEAR THE RABBIT SAY TO ITSELF OH DEAR OH DEAR IS HALL BE LATE WHEN SHE THOUGHT IT OVER AFTERWARDS IT OCCURRED TO HER THAT SHE OUGHT TO HAVE WONDERED AT THIS BUT AT THE TIME IT ALL SEEMED QUITE NATURAL BUT WHEN THE RABBIT ACTUALLY TOOK A WATCH OUT OF ITS WAIST COAT POCKET AND LOOKED AT IT AND THEN HURRIED ON ALICE STARTED TO HER FEET FOR IT FLASHED ACROSS HER MIND THAT SHE HAD NEVER BEFORE SEEN A RABBIT WITH EITHER A WAIST COAT POCKET OR A WATCH TO TAKE OUT OF IT AND BURNING WITH CURIOSITY SHE RAN ACROSS THE FIELD AFTER IT AND FORTUNATELY WAS JUST IN TIME TO SEE IT POP DOWN A LARGE RABBIT HOLE UNDER THE HEDGE