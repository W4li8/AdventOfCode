import numpy as np

input = np.genfromtxt('input.txt', dtype=str)
input = np.array([[int(c) for c in x] for x in input])

tmp = 2**np.arange(input.shape[1])[::-1]  # powers of 2

ans = [0, 0]  # gamma rate, epsilon rate

sum = np.sum(input, 0)
max = input.shape[0]
a = (sum > max/2) * 1
b = 1 - a

ans = [a @ tmp, b @ tmp]

print(f"Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, then multiply them together. What is the power consumption of the submarine? {ans[0] * ans[1]}")

ans = [input, input]  # oxygen generator rating, C02 scrubber rating

for i in range(ans[0].shape[1]):
    sum = np.sum(ans[0], 0)
    max = ans[0].shape[0]
    a = (sum >= max/2) * 1
    ans[0] = ans[0][ans[0].T[i] == a[i]]

    if ans[0].shape[0] == 1:
        break

for i in range(ans[1].shape[1]):
    sum= np.sum(ans[1], 0)
    max = ans[1].shape[0]
    b = 1 - (sum >= max/2) * 1
    ans[1] = ans[1][ans[1].T[i] == b[i]]

    if ans[1].shape[0] == 1:
        break

ans = [ans[0] @ tmp, ans[1] @ tmp]

print(f"Use the binary numbers in your diagnostic report to calculate the oxygen generator rating and CO2 scrubber rating, then multiply them together. What is the life support rating of the submarine? {ans[0] * ans[1]}")
