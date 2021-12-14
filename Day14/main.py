import numpy as np

input0 = input1 = None
with open('input.txt') as file:
    input0 = file.readline()[:-1]
    _ = file.readline()
    input1 = {}
    for line in file:
        k, _ ,v = line[:-1].split(' ')
        input1[k] = v  # input is complete, no edge cases


ans = 0
pairs = {k: 0 for k in input1.keys()}
counter = {k: 0 for k in input1.values()}
counter[input0[0]] += 1
for i in range(len(input0) - 1):
    pairs[input0[i:i+2]] += 1
    counter[input0[i+1]] += 1

for _ in range(10):
    pairs_prev = pairs
    pairs = {k: 0 for k in pairs}
    for k, v in pairs_prev.items():
        i = input1[k]
        pairs[k[0]+i] += v
        pairs[i+k[1]] += v
        counter[i] += v

val = counter.values()
ans = max(val) - min(val)

print(f"Apply 10 steps of pair insertion to the polymer template and find the most and least common elements in the result. What do you get if you take the quantity of the most common element and subtract the quantity of the least common element? {ans}")


ans = 0
pairs = {k: 0 for k in input1.keys()}
counter = {k: 0 for k in input1.values()}
counter[input0[0]] += 1
for i in range(len(input0) - 1):
    pairs[input0[i:i+2]] += 1
    counter[input0[i+1]] += 1

for _ in range(40):
    pairs_prev = pairs
    pairs = {k: 0 for k in pairs}
    for k, v in pairs_prev.items():
        i = input1[k]
        pairs[k[0]+i] += v
        pairs[i+k[1]] += v
        counter[i] += v

val = counter.values()
ans = max(val) - min(val)

print(f"Apply 40 steps of pair insertion to the polymer template and find the most and least common elements in the result. What do you get if you take the quantity of the most common element and subtract the quantity of the least common element? {ans}")
