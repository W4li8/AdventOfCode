import numpy as np

input = None
with open('input.txt') as file:
    input = file.readline()
    input = format(int(input, 16), f"0{(len(input)-1)*4}b")


ans = 0
def decode_packet(packet):
    p, i = packet, 0

    V = int(p[i+0:i+3], 2)
    T = int(p[i+3:i+6], 2)
    i += 6
    if T == 4:
        # literal
        while (I := int(p[i+0], 2)) == 1:
            i += 5
        i += 5
    else:
        # operator
        I = int(p[i+0], 2)
        l = 11 if I == 1 else 15
        L = int(p[i+1:i+l+1], 2)
        i += l + 1

        if I == 1:
            for _ in range(L):
                v, x = decode_packet(p[i:])
                V += v
                i += x
        else:
            j = i + L
            while i < j:
                v, x = decode_packet(p[i:])
                V += v
                i += x

    return V, i

ans, _ = decode_packet(input)
print(f"Decode the structure of your hexadecimal-encoded BITS transmission what do you get if you add up the version numbers in all packets? {ans}")


ans = 0
def decode_packet(packet):
    p, i = packet, 0
    values = []
    _ = int(p[i+0:i+3], 2)
    T = int(p[i+3:i+6], 2)
    i += 6
    if T == 4:
        # literal
        while (I := int(p[i+0], 2)) == 1:
            values.append(p[i+1:i+5])
            i += 5
        values.append(p[i+1:i+5])
        i += 5
        values = int(''.join(values), 2)
    else:
        # operator
        I = int(p[i+0], 2)
        l = 11 if I == 1 else 15
        L = int(p[i+1:i+l+1], 2)
        i += l + 1

        if I == 1:
            for _ in range(L):
                v, x = decode_packet(p[i:])
                values.append(v)
                i += x
        else:
            j = i + L
            while i < j:
                v, x = decode_packet(p[i:])
                values.append(v)
                i += x

        match T:
            case 0: values = np.sum(values)
            case 1: values = np.prod(values)
            case 2: values = np.min(values)
            case 3: values = np.max(values)
            case 5: values = int(values[0] > values[1])
            case 6: values = int(values[0] < values[1])
            case 7: values = int(values[0] == values[1])

    return values, i

ans, _ = decode_packet(input)
print(f"What do you get if you evaluate the expression represented by your hexadecimal-encoded BITS transmission? {ans}")
