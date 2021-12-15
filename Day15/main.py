import numpy as np

input = np.genfromtxt('input.txt', delimiter=1, dtype=int)


Nr, Nc = input.shape
start, target = (0, 0), (Nr-1, Nc-1)

visited = np.zeros_like(input)
riskgrid = np.zeros_like(input) + np.inf

visited[0, 0] = 1
riskgrid[0, 0] = 0
opened = {start}
while len(opened) > 0:
    c = None  # current node
    minrisk = np.inf
    for x in opened:
        if riskgrid[x] <= minrisk:
            c = x
            minrisk = riskgrid[x]

    visited[c] = True
    if c == target:
        break

    i, j = c
    neighbours = set()
    if j+1 < Nc:
        neighbours.add((i, j+1))
    if i > 0:
        neighbours.add((i-1, j))
    if j > 0:
        neighbours.add((i, j-1))
    if i+1 < Nr:
        neighbours.add((i+1, j))

    for n in neighbours:
        if visited[n]:
            continue

        riskgrid[n] = min(riskgrid[n], riskgrid[c] + input[n])
        opened.add(n)

    opened.remove(c)

ans = riskgrid[-1,-1]

print(f"What is the lowest total risk of any path from the top left to the bottom right? {ans}")


scale = 5
input_cp = input
for i in range(1, scale):
    input = np.append(input, input_cp+i, axis=0)
input[input > 9] %= 9
input_cp = input
for j in range(1, scale):
    input = np.append(input, input_cp+j, axis=1)
input[input > 9] %= 9

Nr, Nc = input.shape
start, target = (0, 0), (Nr-1, Nc-1)

visited = np.zeros_like(input)
riskgrid = np.zeros_like(input) + np.inf

visited[0, 0] = 1
riskgrid[0, 0] = 0
opened = {start}
while len(opened) > 0:
    c = None  # current node
    minrisk = np.inf
    for x in opened:
        if riskgrid[x] <= minrisk:
            c = x
            minrisk = riskgrid[x]

    visited[c] = True
    if c == target:
        break

    i, j = c
    neighbours = set()
    if j+1 < Nc:
        neighbours.add((i, j+1))
    if i > 0:
        neighbours.add((i-1, j))
    if j > 0:
        neighbours.add((i, j-1))
    if i+1 < Nr:
        neighbours.add((i+1, j))

    for n in neighbours:
        if visited[n]:
            continue

        riskgrid[n] = min(riskgrid[n], riskgrid[c] + input[n])
        opened.add(n)

    opened.remove(c)

ans = riskgrid[-1,-1]

print(f"Using the full map, what is the lowest total risk of any path from the top left to the bottom right? {ans}")
