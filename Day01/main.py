import numpy as np

input = np.genfromtxt('input.txt', dtype=int)

ans = 0
for i in range(len(input)-1):
    if input[i] < input[i+1]:
        ans += 1

print(f"How many measurements are larger than the previous measurement? {ans}")


ans = 0
for i in range(len(input)-3):
    if np.sum(input[i:i+3]) < np.sum(input[i+1:i+4]):
        ans += 1

print(f"Consider sums of a three-measurement sliding window. How many sums are larger than the previous sum? {ans}")
