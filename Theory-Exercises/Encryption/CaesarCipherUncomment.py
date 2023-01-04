# 1
message = 'The password is 31337'
# 2
key = 20
# 3
mode = 'encrypt' # 4

# 5
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# 6
translated = ''

message = message.upper()

for symbol in message:
# 7
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)
        # 8
        if mode == 'encrypt':
            translatedIndex = symbolIndex + key
        elif mode == 'decrypt':
            translatedIndex = symbolIndex - key
       # 9
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)
        translated = translated + SYMBOLS[translatedIndex]
    else:
       # 10
        translated = translated + symbol
# 11
print(translated)

