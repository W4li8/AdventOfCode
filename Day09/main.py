import numpy as np

input = np.genfromtxt('input.txt', dtype=str)
input = np.array([[int(c) for c in s] for s in input])


mapa = input * 1
mapa[input < 9] = 0
n = 1
lows = []

ans = 0
for i in range(len(input)):
    for j in range(len(input[i])):
        if j+1 < len(input[i]) and input[i][j+1] <= input[i][j]:
            continue
        if i+1 < len(input) and input[i+1][j] <= input[i][j]:
            continue
        if j-1 >= 0 and input[i][j-1] <= input[i][j]:
            continue
        if i-1 >= 0 and input[i-1][j] <= input[i][j]:
            continue

        ans += 1 + input[i][j]

        # data for part 2
        lows = [*lows, [(i, j)]]
        mapa[i][j] = n
        n += 1

print(f"Find all of the low points on your heightmap. What is the sum of the risk levels of all low points on your heightmap? {ans}")


ans = 0
for basin in lows:
    while len(basin) > 0:
        i, j = basin[0]
        if j+1 < len(input[i]) and mapa[i][j+1] == 0 and input[i][j+1] > input[i][j]:
            basin = [*basin, (i, j+1)]
            mapa[i][j+1] = mapa[i,j]
        if i+1 < len(input) and mapa[i+1][j] == 0 and input[i+1][j] > input[i][j]:
            basin = [*basin, (i+1, j)]
            mapa[i+1][j] = mapa[i,j]
        if j-1 >= 0 and mapa[i][j-1] == 0 and input[i][j-1] > input[i][j]:
            basin = [*basin, (i, j-1)]
            mapa[i][j-1] = mapa[i,j]
        if i-1 >= 0 and mapa[i-1][j] == 0 and input[i-1][j] > input[i][j]:
            basin = [*basin, (i-1, j)]
            mapa[i-1][j] = mapa[i,j]

        basin = basin[1:]

_, counts = np.unique(mapa[mapa != 9], return_counts=True)
counts = sorted(counts)

ans = counts[-1] * counts[-2] * counts[-3]

print(f"What do you get if you multiply together the sizes of the three largest basins? {ans}")
