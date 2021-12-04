import numpy as np

numbers = None
boards = []
with open('input.txt') as input:
    numbers = list(map(int, input.readline().split(',')))
    while input.readline():
        boards = [*boards, np.array([
            list(map(int, input.readline().split())),
            list(map(int, input.readline().split())),
            list(map(int, input.readline().split())),
            list(map(int, input.readline().split())),
            list(map(int, input.readline().split()))
        ])]

ans = 0
win = False
for n in numbers:
    for b in boards:
        b[b == n] = -1
        for r, c in zip(b, b.T):
            if np.all(r < 0) or np.all(c < 0):
                win = True
                ans = n * np.sum(b[b > 0])
                break

    if ans != 0:
        break

print(f"To guarantee victory against the giant squid, figure out which board will win first. What will your final score be if you choose that board? {ans}")

ans = 0
win = np.array([False] * len(boards))
for n in numbers:
    for i, b in enumerate(boards):
        if win[i] == False:
            b[b == n] = -1
            for r, c in zip(b, b.T):
                if np.all(r < 0) or np.all(c < 0):
                    win[i] = True
                    if np.all(win == True):
                        ans = n * np.sum(b[b > 0])
                        break

    if ans != 0:
        break

print(f"Figure out which board will win last. Once it wins, what would its final score be? {ans}")
