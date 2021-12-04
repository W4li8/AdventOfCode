import numpy as np

input = np.genfromtxt('input.txt', dtype=None)  # None autodetects (str, int)

ans = [0, 0]  # horizontal, depth
for d, x in input:
    match d:
        case b'forward':
            ans[0] += x
        case b'down':
            ans[1] += x
        case b'up':
            ans[1] -= x

print(f"Calculate the horizontal position and depth you would have after following the planned course. What do you get if you multiply your final horizontal position by your final depth? {ans[0] * ans[1]}")


ans = [0, 0, 0]  # horizontal, depth, aim
for d, x in input:
    match d:
        case b'forward':
            ans[0] += x
            ans[1] += ans[2] * x
        case b'down':
            ans[2] += x
        case b'up':
            ans[2] -= x

print(f"Using this new interpretation of the commands, calculate the horizontal position and depth you would have after following the planned course. What do you get if you multiply your final horizontal position by your final depth? {ans[0] * ans[1]}")
