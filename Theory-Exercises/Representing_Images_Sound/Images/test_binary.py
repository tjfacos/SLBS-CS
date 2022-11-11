bitStream = open("Trees.jpeg", "rb")
count = 0

try:
    bitPattern = bitStream.read(1)
    while bitPattern:
        count += 1
        print(count, ord(bitPattern))
        bitPattern = bitStream.read(1)

finally:
    bitStream.close()