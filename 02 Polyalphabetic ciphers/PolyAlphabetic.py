from Alphabet import Alphabet

# 65 -> A
# 97 -> a
# https://github.com/drewp41/Vigenere-Cipher-Breaker/blob/0eda8f57311e701c46ea77dd56e0394ef98a3f0a/Vigenere_cipher.py#L25

class PolyAlphabetic:
    MAX_KEY_LENGTH_GUESS = 30

    def __init__(self, cipher_path):
        self.cipher_path = cipher_path

        f = open(cipher_path, "r")
        self.cipher = f.read()
        f.close()

        print(self.cipher)

        self.dict_replace = {}
        self.decrypted = ""

    # metodo iniziale per calcolare la lunghezza della chiave
    # Returns the key length with the highest average Index of Coincidence
    def get_key_length(self):
        ic_table = []
        ciphertext = self.cipher

        # Splits the ciphertext into sequences based on the guessed key length from 0 until the max key length guess (20)
        # Ex. guessing a key length of 2 splits the "12345678" into "1357" and "2468"
        # This procedure of breaking ciphertext into sequences and sorting it by the Index of Coincidence
        # The guessed key length with the highest IC is the most porbable key length
        for guess_len in range(PolyAlphabetic.MAX_KEY_LENGTH_GUESS):
            ic_sum = 0.0
            avg_ic = 0.0
            for i in range(guess_len):
                sequence = ""
                # breaks the ciphertext into sequences
                for j in range(0, len(ciphertext[i:]), guess_len):
                    sequence += ciphertext[i + j]
                ic_sum += self.get_index_c(sequence)
            # obviously don't want to divide by zero
            if not guess_len == 0:
                avg_ic = ic_sum / guess_len # qui giustamente fa una cazzo di media per stabiliare l'indice di incidenza medio
            ic_table.append(avg_ic)

        # e giustamente prende i 2 indici di incidenza medi maggiori
        # returns the index of the highest Index of Coincidence (most probable key length)
        best_guess = ic_table.index(sorted(ic_table, reverse=True)[0])
        second_best_guess = ic_table.index(sorted(ic_table, reverse=True)[1])

        print(f"best_guess: {best_guess}")
        print(f"second_best_guess: {second_best_guess}")

        # Since this program can sometimes think that a key is literally twice itself, or three times itself,
        # it's best to return the smaller amount.
        # Ex. the actual key is "dog", but the program thinks the key is "dogdog" or "dogdogdog"
        # (The reason for this error is that the frequency distribution for the key "dog" vs "dogdog" would be nearly identical)
        if best_guess % second_best_guess == 0:
            return second_best_guess
        else:
            return best_guess

    # usato da get_key_length per calcolare l'indice di coincidenza (la parola compare più volte)
    # Returns the Index of Councidence for the "section" of ciphertext given
    def get_index_c(self, ciphertext):
        N = float(len(ciphertext))
        frequency_sum = 0.0

        # Using Index of Coincidence formula
        for letter in Alphabet.CHARACTERS:
            frequency_sum += ciphertext.count(letter) * (ciphertext.count(letter) - 1)

        # Using Index of Coincidence formula
        ic = frequency_sum / (N * (N - 1))
        return ic


    # con la lunghezza della chiave, spezza il cifrario in blocchi e sfrutta l'analisi di frequenza inglese
    # per stabilire quale carattere sia migliore per la chiave
    def get_key(self, key_length):
        ciphertext = self.cipher
        key = ''

        # Calculate letter frequency table for each letter of the key
        for i in range(key_length):
            sequence = ""
            # breaks the ciphertext into sequences
            for j in range(0, len(ciphertext[i:]), key_length):
                sequence += ciphertext[i + j]
            key += self.freq_analysis(sequence)

        return key

    def freq_analysis(self, sequence):
        all_chi_squareds = [0] * 26

        for i in range(26):

            chi_squared_sum = 0.0

            # sequence_offset = [(((seq_ascii[j]-97-i)%26)+97) for j in range(len(seq_ascii))]
            # sequence_offset = [chr(((ord(sequence[j]) - 97 - i) % 26) + 97) for j in range(len(sequence))]
            sequence_offset = [chr(((ord(sequence[j]) - 65 - i) % 26) + 65) for j in range(len(sequence))]
            v = [0] * 26
            # count the numbers of each letter in the sequence_offset already in ascii
            for l in sequence_offset:
                # v[ord(l) - ord('a')] += 1
                v[ord(l) - ord('A')] += 1
            # divide the array by the length of the sequence to get the frequency percentages
            for j in range(26):
                v[j] *= (1.0 / float(len(sequence)))

            # now you can compare to the english frequencies
            for j in range(26):
                chi_squared_sum += ((v[j] - float(Alphabet.ENGLISH_FREQUENCIES[j])) ** 2) / float(Alphabet.ENGLISH_FREQUENCIES[j])

            # add it to the big table of chi squareds
            all_chi_squareds[i] = chi_squared_sum

        # return the letter of the key that it needs to be shifted by
        # this is found by the smallest chi-squared statistic (smallest different between sequence distribution and
        # english distribution)
        shift = all_chi_squareds.index(min(all_chi_squareds))

        # return the letter
        # return chr(shift + 97)
        return chr(shift + 65)

    # Returns the plaintext given the ciphertext and a key
    def decrypt(self, key):
        ciphertext = self.cipher
        # Creates an array of the ascii values of the ciphertext and the key
        cipher_ascii = [ord(letter) for letter in ciphertext]
        key_ascii = [ord(letter) for letter in key]
        plain_ascii = []

        # Turns each ascii value of the ciphertext into the ascii value of the plaintext
        for i in range(len(cipher_ascii)):
            plain_ascii.append(((cipher_ascii[i] - key_ascii[i % len(key)]) % 26) + 65)

        # Turns the array of ascii values into characters
        plaintext = ''.join(chr(i) for i in plain_ascii)
        return plaintext
