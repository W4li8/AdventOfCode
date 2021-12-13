import numpy as np

input0 = np.genfromtxt('input.txt', dtype=int, delimiter=',', skip_footer=12)
input1 = np.genfromtxt('input.txt', dtype=str, skip_header=len(input0)).T[-1]


ans = 0
n_indices = set(map(tuple, input0))
for fold in input1:
    m = int(fold[2:])
    p = []
    n = []
    for i, j in n_indices:
        if fold[0] == 'x' and i > m:
            p.append((2*m - i, j))
            n.append((i, j))
        if fold[0] == 'y' and j > m:
            p.append((i, 2*m - j))
            n.append((i, j))

    for pi in p:
        n_indices.add(pi)

    for ni in n:
        n_indices.remove(ni)

    break  # do just first one

ans = len(n_indices)

print(f"How many dots are visible after completing just the first fold instruction on your transparent paper? {ans}")


ans = 0
n_indices = set(map(tuple, input0))
for fold in input1:
    m = int(fold[2:])
    p = []
    n = []
    for i, j in n_indices:
        if fold[0] == 'x' and i > m:
            p.append((2*m - i, j))
            n.append((i, j))
        if fold[0] == 'y' and j > m:
            p.append((i, 2*m - j))
            n.append((i, j))

    for pi in p:
        n_indices.add(pi)

    for ni in n:
        n_indices.remove(ni)

n_indices = np.array(list(map(list, n_indices)))
disp = np.zeros((np.max(n_indices.T[0])+1, np.max(n_indices.T[1])+1), dtype=int)
for i, j in n_indices:
    disp[i,j] = 1

print(disp.T, f"\nWhat code do you use to activate the infrared thermal imaging camera system? 'FAGURZHE' (read from array print)")
