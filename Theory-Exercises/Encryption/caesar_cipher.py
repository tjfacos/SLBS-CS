def shift(plain, vect=5):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    length = len(alphabet)
    ciphertext = ""
    
    v = vect % length
    print(v)

    if v < 0:
        v = length - v
    
    

    for character in plain:
        index = alphabet.find(character)
    
        if index == -1:
            ciphertext += character
        elif vect < 0:
            ciphertext += alphabet[(index+v) % length]
        else:
            i = index - v
            if i < 0:
                i += length
            ciphertext += alphabet[i]

    return ciphertext

if __name__ == "__main__":
    cipher = shift("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG", vect=26)
    plain = shift(cipher, vect=-3)
    #broken, negative/positive currently doesn't matter (always shifts left)
    print(cipher)
    print(plain)
    # If vect > 0, shift to the right
    # If vect < 0, shift to the left
