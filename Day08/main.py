import numpy as np

input = np.genfromtxt('input.txt', delimiter=' ', dtype=str)
input = np.delete(input, 10, axis=1)

seg7 = {
    0: 'abcefg',
    1: 'cf',
    2: 'acdeg',
    3: 'acdfg',
    4: 'bcdf',
    5: 'abdfg',
    6: 'abdefg',
    7: 'acf',
    8: 'abcdefg',
    9: 'abcdfg'
}

ans = 0
for x in input:
    for k in x[-4:]:
        if len(k) in [len(seg7[1]), len(seg7[4]), len(seg7[7]), len(seg7[8])]:
            ans += 1

print(f"In the output values, how many times do digits 1, 4, 7, or 8 appear? {ans}")


ans = 0
for x in input:
    x = [''.join(sorted(ni)) for ni in x]
    x[:10] = sorted(x[:10], key=len)

    # decode 7seg -- n numbers dict, c char map
    n = {1: x[0], 4: x[2], 7: x[1], 8: x[9]}
    for ni in x[3:6]:
        if set(n[1]).issubset(set(ni)):
            n[3] = ni  # is unique

    for ni in x[6:9]:
        if not set(n[1]).issubset(set(ni)):
            n[6] = ni  # is unique

    c = {}
    c['a'] = set(n[7]).difference(set(n[1]))
    c['c'] = set(n[8]).difference(set(n[6]))
    c['f'] = set(n[1]).difference(c['c'])
    c['b'] = set(n[4]).difference(set(n[3]))
    c['e'] = set(n[8]).difference(set(n[3])) \
                      .difference(c['b'])
    c['d'] = set(n[4]).difference(set(n[1])) \
                      .difference(c['b'])
    c['g'] = set(n[8]).difference(set(n[4])) \
                      .difference(c['a']) \
                      .difference(c['e'])

    n[2] = ''.join(set(n[8]).difference(c['b']).difference(c['f']))
    n[5] = ''.join(set(n[8]).difference(c['c']).difference(c['e']))
    n[0] = ''.join(set(n[8]).difference(c['d']))
    n[9] = ''.join(set(n[8]).difference(c['e']))

    # rearrange keys for indexing, match sort at loop start
    for k in n:
        n[k] = ''.join(sorted(n[k]))

    n = dict([(value, key) for key, value in n.items()])
    ans += 1000*n[x[-4]] + 100*n[x[-3]] + 10*n[x[-2]] + n[x[-1]]

print(f"For each entry, determine all of the wire/segment connections and decode the four-digit output values. What do you get if you add up all of the output values? {ans}")
