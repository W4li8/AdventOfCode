import numpy as np

input = np.genfromtxt('input.txt', delimiter=',', dtype=int)

ages, fishes = np.unique(input, return_counts=True)
population = dict(zip(range(9), np.zeros(9, dtype= int)))

for age, count in zip(ages, fishes):
    population[age] = count

for _ in range(80):
    p_next = dict(zip(range(9), np.zeros(9, dtype=int)))
    # print(population)
    for k in population.keys():
        # print(k)
        if k == 0:
            p_next[8] += population[0]
            p_next[6] += population[0]
        else:
            p_next[k-1] += population[k]

    population = p_next

ans = np.sum(list(population.values()))

print(f"Find a way to simulate lanternfish. How many lanternfish would there be after 80 days? {ans}")


population = dict(zip(range(9), np.zeros(9, dtype=int)))

for age, count in zip(ages, fishes):
    population[age] = count

for _ in range(256):
    p_next = dict(zip(range(9), np.zeros(9, dtype=int)))
    # print(population)
    for k in population.keys():
        # print(k)
        if k == 0:
            p_next[8] += population[0]
            p_next[6] += population[0]
        else:
            p_next[k-1] += population[k]

    population = p_next

ans = np.sum(list(population.values()))

print(f"How many lanternfish would there be after 256 days? {ans}")
