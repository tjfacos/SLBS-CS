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

# def decodeTranspose(text, key):
#     plaintext = ""

#     grid_x = key
#     grid_y = int(len(text)/key)
#     if grid_y != len(text)/key:
#         grid_y += 1
    
#     grid = [["" for x in range(grid_x)] for y in range(grid_y)]
#     i = 0
#     for x in range(grid_x):
#         for y in range(grid_y):
#             if i >= len(text):
#                 grid[y][key*y] = ""
#             else:
#                 print(key*y+x)
#                 grid[y][key*y] = list(text)[i+x]
#             i += 1
    
#     print(grid)
#     for row in grid:
#         plaintext += ''.join(row)
   
#     return plaintext



if __name__ == "__main__":
    returned  = transpose("helloworld", 4)
    print(returned)
    # print(decodeTranspose(returned, 4))