def transpose(text, key):
    ciphertext = ""
    grid = []
    for i in range(0, len(text), key):
        if i+key > len(text):
            grid.append(list(text[i:]))
        else:
            grid.append(list(text[i: i+key]))

    while len(grid[0]) != len(grid[-1]):
        grid[-1].append("")

    # print(grid)
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            ciphertext += grid[y][x]
    
    return ciphertext

def decodeTranspose(text, key):
    pass


if __name__ == "__main__":
    returned  = transpose("helloworld", 4)
    print(returned)
    # print(decodeTranspose(returned, 4))