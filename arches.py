from random import choice
from time import time
from decimal import Decimal as long



class ArchesCrypto():

    def __init__(self, to_encode = None):

        # letters that serve as the random part of the encoding
        self.letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p')

        # letters that serve as the index of the encoded chars
        self.index_letters = ('Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r')

        # same as above but with Q (means space)
        self.Qindex_letters = ('Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'Q')

        # chars that are encoded
        self.supported_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz '

        # dict matching encoded letters, ex.: yaaa -> dict.get('y')[2]
        # means: get key <index letter> and at its list, get the third item
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

        # if the class call had any param, encode it, else do nothing
        self.encode(to_encode) if to_encode is not None else 0 



    def generate_char(self, index_letter, times):
        # translate the chars recieving the index letter and the number of random chars it should generate
        # input: y, 1
        # output: ya

        random_letters = []
        # x times, add a random letter
        for _ in range(times):
            random_letters.append(choice(self.letters))

        # return index letter + random_letters list as a joined string
        return index_letter + str().join(random_letters)



    def encode(self, to_encode):

        encoding = []
        # for each char in to_encode, ascii-encode it 
        for letter in to_encode:
            encoding.append(ord(letter))

        for item in encoding:
            
            down_limit = 65 # ascii matching to A
            up_limit = 67

            flagged_found = False # goes True when the char is encoded

            for letter in self.index_letters:
            # tests all index letters

                if letter == 'y': #ascii shit
                    down_limit += 6
                    up_limit += 6
        
                up_limit += 1 if letter.upper() in 'TR' else 0 
                # on T and R letters, there is plus one random possible letter 
                
                if item >= down_limit and item <= up_limit:
                    self.encoded.append(self.generate_char(letter, item-(down_limit-1)))
                    # if the ascii code is between the limits of the index letter, i.e. abc (y), def(w), etc
                    # then encode generating the random chars 
                    flagged_found = True # flags that it has encoded to further assignments
                    break # dont need to continue the loop testing letters since it already encoded
                
                down_limit += 1 if letter.upper() in 'TR' else 0 # same as the other
                down_limit += 3
                up_limit += 3
                # limit increment for looping the letters on ascii code 

            if not flagged_found:
                # if the char was not encoded, checks if it's space, if it isnt, just put the char anyway 
                if item == 32:
                    self.encoded.append('Q')
                else:
                    self.encoded.append(chr(item)) 
                    # python has built-in functions chr() and ord() to translating ascii
                    # py goals 

        # encoded var is a list, converts it to a string before returning it
        self.encoded = str().join(self.encoded)
        return self.encoded



    def decode(self, decoding = None):

        decoding = self.encoded if decoding is None else decoding
        # decoding recieves what is already encoded at the object if no entry is given at the decoding parameter

        char_indexes = []
        disjoined_chars = []

        # for each char inside decoding that is a index letter, appends the char index to a list
        for char in range(len(decoding)):
            if decoding[char] in self.Qindex_letters:
                char_indexes.append(char) # appends only the index of the index letter to the list

        # at the end, certifies that the indexes are on crescent order sorting the list
        char_indexes.sort() # in the end it doesnt do anything kkkkkkkkkkkkkkkkkkkkkkkkkk ill leave it there just cuz its fun


        # for each index in the list, do
        for i in range(len(char_indexes)):
            
            try: # append the letters between each section of the indexes to disjoin each whole char
                disjoined_chars.append(decoding[char_indexes[i]:char_indexes[i+1]])
            except IndexError:
                disjoined_chars.append(decoding[char_indexes[i]:])

        ### just a management to ignore non encoded chars in the input shit
        non_encoded_chars = []
        for item in range(len(disjoined_chars)):

            non_encoded_chars.append([])

            for char in disjoined_chars[item]:

                if char not in self.supported_letters:
                    non_encoded_chars[-1].append(char)
                    disjoined_chars[item] = disjoined_chars[item].replace(char, '')

            non_encoded_chars.append([]) if non_encoded_chars[-1] != [] else 0 
       
        for item in range(len(non_encoded_chars)):
            if non_encoded_chars[item] != []:
                disjoined_chars.insert(item+1, str().join(non_encoded_chars[item]))
        ###

        decoding = disjoined_chars
        #print(decoding)
        for item in decoding:
            if item[0] in self.Qindex_letters:
                translated_letter = self.index_match_dict.get(item[0])[len(item)-2] # matching chars with the dict at __init__
                self.decoded.append(translated_letter)
            else:
                self.decoded.append(item)

        self.decoded = str().join(self.decoded)        
        return self.decoded



    def to_alphadecimal(self, to_convert):

        alphadecimal = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        base = len(alphadecimal) ## 62
        result = ''

        # because it's needed to treat zero before the loop
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

    # 
    # average 82ms to encode  itself (on i3-2330M)
    file = open('archesHash.py', 'r').read()
    itself = ArchesCrypto().encode(file)
    
    open('itself_encoded', 'w').write(itself)
    open('itself.py', 'w').write(ArchesCrypto().decode(itself))
    

    


    
