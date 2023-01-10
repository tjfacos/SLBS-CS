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
    grid_x = key
    grid_y = len(text) / key
    if grid_y % 1 != 0:
        grid_y = int(grid_y ) + 1

    grid = [["" for x in range(grid_x )] for y in range(grid_y )]
    # print(grid)
    
    for a in range(len(text)):
        #print(a)
        #print(a//key)
        #print(a%key)
        grid[a//key][a%key] = "p"
    
    # print(grid)
    # print(len(text))
    i = 0
    for x in range(grid_x):
        for y in range(grid_y):
        #    print(x,y)
           if grid[y][x]:
                grid[y][x] = text[i]
                i += 1
                
    # print(grid )
    
    plaintext = ""
    for row in grid:
        plaintext += ''.join(row)

    return plaintext



if __name__ == "__main__":
    returned  = transpose("helloworld", 4)
    print(returned)
    print(decodeTranspose(returned, 4))