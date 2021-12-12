import numpy as np

input = np.genfromtxt('input.txt', dtype=int, delimiter=1)

def inc_adjacent(grid, x, y):
    for i in x + np.array([-1, 0, 1]):
        if i >= 0 and i < len(grid):
            for j in y + np.array([-1, 0, 1]):
                if j >= 0 and j < len(grid[i]):
                    grid[i, j] += 1


ans = 0
grid = input * 1
for _ in range(100):
    grid += 1
    flash = grid * 0
    while True:
        x, y = np.where(grid * (1 - flash) > 9)

        if len(x) == 0:
            break

        for i, j in zip(x.T, y.T):
            inc_adjacent(grid, i, j)
            flash[i, j] = 1

    grid[flash > 0] = 0
    ans += np.sum(flash)

print(f"Given the starting energy levels of the dumbo octopuses in your cavern, simulate 100 steps. How many total flashes are there after 100 steps? {ans}")


ans = 0
grid = input * 1
while True:
    grid += 1
    flash = grid * 0
    while True:
        x, y = np.where(grid * (1 - flash) > 9)

        if len(x) == 0:
            break

        for i, j in zip(x.T, y.T):
            inc_adjacent(grid, i, j)
            flash[i, j] = 1

    ans += 1
    if np.all(flash > 0):
        break

    grid[flash > 0] = 0

print(f"If you can calculate the exact moments when the octopuses will all flash simultaneously, you should be able to navigate through the cavern. What is the first step during which all octopuses flash? {ans}")
