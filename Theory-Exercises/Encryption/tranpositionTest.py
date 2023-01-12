from transposition import *
from random import randint, choice, seed



def test():
    passed = True

    seed(1234567)

    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i in range(20):
        message_length = randint(10, 100)
        message = ""

        for c in range(message_length):
            message += choice(letters)
        print(f"Test {i+1}: {message}")
        
        for key in range(1, message_length):
            encrypted = transpose(message, key)
            if decodeTranspose(encrypted, key) == message:
                print("pass")
            else:
                print(f"Failed: {encrypted} {decodeTranspose(encrypted, key)}")
                passed = False
        
    if passed:
        print("TOTAL PASS")

test()