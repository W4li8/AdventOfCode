import numpy as np

input = []
with open('input.txt') as file:
    for line in file:
        input = [*input, list(map(int, line.replace('->', ',').split(',')))]

input = np.array(input)
size = np.max(input)

grid = np.zeros((size, size))
ans = 0
for line in input:
    x1, y1, x2, y2 = line
    dx = x2 - x1
    dy = y2 - y1
    sx = np.sign(dx)
    sy = np.sign(dy)

    if sx == 0 and sy == 0:
        grid[x1-1][y1-1] += 1
        continue

    rangex = range(x1, x2 + sx, sx if sx != 0 else 1)
    rangey = range(y1, y2 + sy, sy if sy != 0 else 1)

    if dx != 0 and dy != 0:
        pass

    elif dy == 0:
        for x in rangex:
            grid[x-1][y1-1] += 1

    elif dx == 0:
        for y in rangey:
            grid[x1-1][y-1] += 1
    else:
        pass

ans = np.count_nonzero(grid[grid > 1])

print(f"Consider only horizontal and vertical lines. At how many points do at least two lines overlap? {ans}")


grid = np.zeros((size, size))
ans = 0
for line in input:
    x1, y1, x2, y2 = line
    dx = x2 - x1
    dy = y2 - y1
    sx = np.sign(dx)
    sy = np.sign(dy)

    if sx == 0 and sy == 0:
        grid[x1-1][y1-1] += 1
        continue

    rangex = range(x1, x2 + sx, sx if sx != 0 else 1)
    rangey = range(y1, y2 + sy, sy if sy != 0 else 1)

    if dx != 0 and dy != 0:
        for x, y in zip(rangex, rangey):
            grid[x-1][y-1] += 1

    elif dy == 0:
        for x in rangex:
            grid[x-1][y1-1] += 1

    elif dx == 0:
        for y in rangey:
            grid[x1-1][y-1] += 1
    else:
        pass

ans = np.count_nonzero(grid[grid > 1])

print(f"Consider all of the lines. At how many points do at least two lines overlap? {ans}")
