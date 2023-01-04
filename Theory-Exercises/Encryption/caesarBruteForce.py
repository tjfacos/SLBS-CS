from caesar_cipher import shift

cipher = input("Enter cipher: ")

for i in range(26):
    print(shift(cipher, vect=i, mode="decrypt"))