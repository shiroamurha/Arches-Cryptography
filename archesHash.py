from random import choice
from time import time
from decimal import Decimal as long



class ArchesCrypto():

    def __init__(self, to_encode = None):

        self.letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p')
        self.index_letters = ('Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r')
        self.Qindex_letters = ('Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'Q')
        self.supported_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz '

        self.index_match_dict = {

            'Y': ['A', 'B', 'C'],
            'X': ['D', 'E', 'F'],
            'W': ['G', 'H', 'I'],
            'V': ['J', 'K', 'L'],
            'U': ['M', 'N', 'O'],
            'T': ['P', 'Q', 'R', 'S'],
            'S': ['T', 'U', 'V'],
            'R': ['W', 'X', 'Y', 'Z'],

            'y': ['a', 'b', 'c'],
            'x': ['d', 'e', 'f'],
            'w': ['g', 'h', 'i'],
            'v': ['j', 'k', 'l'],
            'u': ['m', 'n', 'o'],
            't': ['p', 'q', 'r', 's'],
            's': ['t', 'u', 'v'],
            'r': ['w', 'x', 'y', 'z'],

            'Q': [' '] 
        }
        
        self.encoded = []
        self.decoded = []

        self.encode(to_encode) if to_encode is not None else 0 

    def __str__(self):
        return self.encoded

    def generate_char(self, index_letter, times):

        random_letters = []
        for _ in range(times):
            random_letters.append(choice(self.letters))

        return index_letter + str().join(random_letters)

    def encode(self, to_encode):

        encoding = []
        for letter in to_encode:
            encoding.append(ord(letter))

        for item in encoding:

            down_limit = 65
            up_limit = 67
            flagged_found = False

            for letter in self.index_letters:

                if letter == 'y':
                    down_limit += 6
                    up_limit += 6
        
                up_limit += 1 if letter.upper() in 'TR' else 0
                #print(down_limit, up_limit)
                if item >= down_limit and item <= up_limit:
                    self.encoded.append(self.generate_char(letter, item-(down_limit-1)))
                    
                    flagged_found = True
                    break
                
                down_limit += 1 if letter.upper() in 'TR' else 0
                down_limit += 3
                up_limit += 3

            if not flagged_found:

                if item == 32:
                    self.encoded.append('Q')
                else:
                    self.encoded.append(chr(item))


        self.encoded = str().join(self.encoded)
 
    def decode(self, decoding = None):

        decoding = self.encoded if decoding is None else decoding
        char_indexes = []
        disjoined_chars = []


        for char in range(len(decoding)):
            if decoding[char] in self.Qindex_letters:
                char_indexes.append(char)
        char_indexes.sort()

        for i in range(len(char_indexes)):

            try:
                disjoined_chars.append(decoding[char_indexes[i]:char_indexes[i+1]])
            except IndexError:
                disjoined_chars.append(decoding[char_indexes[i]:])

        non_encoded_chars = []
        for item in range(len(disjoined_chars)):

            non_encoded_chars.append([])

            for char in disjoined_chars[item]:

                if char not in self.supported_letters:
                    non_encoded_chars[-1].append(char)
                    disjoined_chars[item] = disjoined_chars[item].replace(char, '')

            non_encoded_chars.append([]) if non_encoded_chars[-1] != [] else 0 
        #print(non_encoded_chars)

        for item in range(len(non_encoded_chars)):
            if non_encoded_chars[item] != []:
                disjoined_chars.insert(item+1, str().join(non_encoded_chars[item]))

        decoding = disjoined_chars
        #print(decoding)
        for item in decoding:
            if item[0] in self.Qindex_letters:
                translated_letter = self.index_match_dict.get(item[0])[len(item)-2]
                self.decoded.append(translated_letter)
            else:
                self.decoded.append(item)

        self.decoded = str().join(self.decoded)        
        return self.decoded

    def hash_it(self, to_hash = None):

        number_cluster = []
        sliced_cluster = []

        to_hash = self.encoded if to_hash is None else 0        

        first_number_cluster = list(str().join([str(ord(letter)) for letter in to_hash]))
        number_cluster = first_number_cluster
        pintched_cluster = []

        while len(number_cluster) > 460:
            pintched_cluster = [number_cluster[i] for i in range(0, len(number_cluster), 2)]
            number_cluster = pintched_cluster

        while len(number_cluster) != 459:
            for i in range(0, 459 - len(number_cluster), 7):
                number_cluster.append(first_number_cluster[i])

        self.hash = int(str().join(number_cluster))
        self.hash = self.to_alphadecimal(self.hash)

        return self.hash

    def to_alphadecimal(self, to_convert):

        alphadecimal = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        base = len(alphadecimal) ## 62
        result = ''

        # because need to treat zero before the loop
        resto = to_convert % base
        result = alphadecimal[resto] + result
        to_convert = to_convert // base

        while to_convert > 0:
            resto = to_convert % base
            result = alphadecimal[resto] + result
            to_convert = to_convert // base

        return result

       

#    
#
#
if __name__== "__main__":
    tempo = time()
    v = ArchesCrypto(open('archesHash.py', 'r').read())
    open('hashed.txt', 'w').write(v.hash_it())
    print(time()-tempo)
    

    


    