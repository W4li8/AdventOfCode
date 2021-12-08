import numpy as np

input = np.genfromtxt('input.txt', delimiter=',', dtype=int)

ans = np.inf
for i in range(np.max(input)+1):
    cost = np.sum(np.abs(input - i))
    if cost < ans:
        ans = cost

print(f"Determine the horizontal position that the crabs can align to using the least fuel possible. How much fuel must they spend to align to that position? {ans}")


ans = np.inf
for i in range(np.max(input)+1):
    n = np.abs(input - i)
    cost = 0.5*n@(n + 1)
    if cost < ans:
        ans = cost

print(f"Determine the horizontal position that the crabs can align to using the least fuel possible so they can make you an escape route! How much fuel must they spend to align to that position? {ans}")
