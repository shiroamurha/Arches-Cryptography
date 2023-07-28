from random import choice
from time import time



class ArchesHash():

    def __init__(self, to_encode: str):

        self.letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p')
        self.index_letters = ('Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r')
        self.encoding = []
        self.encoded = []

        self.to_encode = to_encode

        self.encode()

    def __str__(self):
        return self.encoded

    def generate_char(self, index_letter, times):

        random_letters = []
        for _ in range(times):
            random_letters.append(choice(self.letters))

        return index_letter + str().join(random_letters)

    def encode(self):

        for letter in self.to_encode:
            self.encoding.append(ord(letter))

        for item in self.encoding:

            down_limit = 65
            up_limit = 67

            for letter in self.index_letters:

                if letter == 'y':
                    down_limit += 6
                    up_limit += 7
        
                up_limit += 1 if letter.upper() in 'TR' else 0

                if item >= down_limit and item <= up_limit:
                    self.encoded.append(self.generate_char(letter, item-(down_limit-1)))
                    break
                
                down_limit += 1 if letter.upper() in 'TR' else 0
                down_limit += 3
                up_limit += 3

        self.encoded = str().join(self.encoded)
 

    

#
if __name__== "__main__":
    palavra = ArchesHash('oi')  
    print(palavra)
    


    