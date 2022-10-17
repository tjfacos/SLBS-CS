def apply_weights(array, weights):
    new_array = []

    for i in range(len(array)):
        new_array.append(array[i] * weights[i])

    return new_array

def ISBN():

    isbn = list(map(int, input("Enter ISBN: ")))

    if not isbn:
        isbn = list(map(int, "9780956143051")) #Valid under ISBN-13

    print(f"ISBN: {isbn}")

    if len(isbn) == 10: #ISBN-10
        print('Using ISBN-10:')
        print("ISBN code is: ", end="")
        weights = [x for x in range(10,0,-1)]
        sum = 0
        for item in apply_weights(isbn, weights):
            sum += item

        print(f"Sum: {sum}")

        valid = sum % 11 == 0
        if valid:
            print('Valid')
        else:
            print('Invalid')

    elif len(isbn) == 13: #ISBN-13
        print('Using ISBN-13')
        print("ISBN code is: ", end="")

        weights = [1 if x%2==0 else 3 for x in range(12) ]

        sum = 0
        for item in apply_weights(isbn, weights):
            sum += item

        valid = 10 - (sum % 10) == isbn[12]
        if valid:
            print('Valid')
        else:
            print('Invalid')

    else:
        print('Invalid')
    
    return isbn, valid


if __name__ == "__main__":
    print(
        ISBN()
    )