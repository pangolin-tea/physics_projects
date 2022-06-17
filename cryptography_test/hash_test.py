import numpy as np


# required minimum length of password 8, make the encryption based on the hash of the given password
# note: cannot unhash password
# create own hash algorithm?

def enc1(password):
    numb = np.abs(hash(password))
    encrypt = numb
    return encrypt


def dec(password):
    return


def hashing_test(password):
    alphabet = []
    for x in range(65, 91):
        alphabet.append(chr(x))
    matrix = []
    row = []
    n = 0
    for x in range(26):
        for y in range(26):
            row.append(str(n))
            n += 1
        matrix.append(row)
        row = []
    for x in matrix:
        print(x)
    print(alphabet)
    return


hashing_test(input('Enter password: '))
