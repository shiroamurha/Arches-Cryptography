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

    return [result, time()-tempo] 

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

    return [result, time()-tempo] 

a = to_alphadecimal(64**256)[0]
print(a)
a = to_alphadecimal(int(a))[0]
print(a)


#print(f'{a}\n{b}')


