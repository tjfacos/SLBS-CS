def shift(plain, vect=5, mode=""):
    v_temp = vect
    
    #Make args
    #integrate uppercase, lowercase, and special characters

    if mode == "decrypt":
        v_temp *= -1
    
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    length = len(alphabet)
    ciphertext = ""
    
    v = v_temp % length

    for character in plain:
        index = alphabet.find(character)
    
        if index == -1:
            ciphertext += character
        else:
            newindex = (index + v)%length
            ciphertext += alphabet[newindex]

    return ciphertext

if __name__ == "__main__":
    cipher = shift(input(), vect=6)
    plain = shift(cipher, vect=6, mode="decrypt")
    #broken, negative/positive currently doesn't matter (always shifts left)
    print(cipher)
    print(plain)
    
    # If vect > 0, shift to the right
    # If vect < 0, shift to the left
