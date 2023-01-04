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
        lower = False
        if character != character.upper():
            lower = True
        
        
        index = alphabet.find(character.upper())
    
        if index == -1:
            ciphertext += character
        else:
            newindex = (index + v)%length
            newchar = alphabet[newindex]
            if lower: newchar = newchar.lower()
            ciphertext += newchar

    return ciphertext

if __name__ == "__main__":
    print(shift("The password is 31337", vect=20))
    
    # If vect > 0, shift to the right
    # If vect < 0, shift to the left
