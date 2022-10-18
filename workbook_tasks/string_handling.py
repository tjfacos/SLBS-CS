string = input("Enter String: ")

for i in range(1, len(string)+1):
    print(string[-1*i], end="")

print()