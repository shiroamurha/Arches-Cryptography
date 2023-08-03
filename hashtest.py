from time import time



def to_alphadecimal(to_convert):

    tempo = time()
    alphadecimal = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_"
    base = len(alphadecimal) ## 64
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

def to_decimal(to_convert):

    tempo = time()
    to_convert = list(to_convert)
    to_convert.reverse()
    alphadecimal = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_"
    base = len(alphadecimal) ## 64
    result = 0

    for digit in range(len(to_convert)):
        result += alphadecimal.index(to_convert[digit])*(base**digit)
        # corresponding value of the digit times (base^n-1 digit position) 

    return result 

def re_hash(hashed):
    open('h.txt', 'w').write(' ')
    digits_string = ''
    for item in hashed:
        ascii_digit = str(ord(item))
        # if len(ascii_digit) < 3:
        #     ascii_digit = list(ascii_digit)
        #     ascii_digit.insert(0, '0')
        #     ascii_digit = str().join(ascii_digit)
        digits_string += ascii_digit

    if len(digits_string) < 4300:
        return re_hash(to_alphadecimal(int(digits_string))) # if 1st digit is 0 it will be stripped out

    else:
        while True:
            hashed = digits_string
            digits_string = ''

            for item in hashed:
                ascii_digit = str(ord(item))
                # if len(ascii_digit) < 3:
                #     ascii_digit = list(ascii_digit)
                #     ascii_digit.insert(0, '0')
                #     ascii_digit = str().join(ascii_digit)
                digits_string += ascii_digit

            new_splitted_digits = []


            for index in range(0, len(digits_string), 18):
                try:
                    new_splitted_digits.append(
                        to_alphadecimal( 
                            int( digits_string[ index : index + 18 ])
                        )
                    )
                except IndexError:
                    new_splitted_digits.append(
                        to_alphadecimal(
                            int( digits_string[ index :])
                        )
                    )

            digits_string = str().join(new_splitted_digits)

            if len(digits_string) <= 256:
                return digits_string
            else:
                file = open('h.txt', 'r').read()
                file += f'\n\n {digits_string}'
                open('h.txt', 'w').write(file)

            
        



a = re_hash(to_alphadecimal(64**256))


#print(f'{a} \n\n {re_hash(a)}')
