with open("AlanTuring.txt") as f:
    text = f.read()
    text = text.upper()

# print(text)

def get_letter_frequencies(text):
    freq_dict = {}

    for letter in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            freq_dict[letter] = list(text).count(letter)/len(text)
        
    return freq_dict
        
print(get_letter_frequencies(text))