import numpy as np

input = np.genfromtxt('input.txt', dtype=str)

ord = {'(': ')', '[': ']', '{': '}', '<': '>'}
opp = {')': '(', ']': '[', '}': '{', '>': '<'}
err = {')': 3, ']': 57, '}': 1197, '>': 25137}
mis = {')': 1, ']': 2, '}': 3, '>': 4}


ans = 0
for line in input:
    stack = []
    for c in line:
        if c in ['(', '[', '{', '<']:
            stack.append(c)
        elif len(stack) > 0 and opp[c] == stack[-1]:
            stack.pop()
        else:
            ans +=err[c]
            break

print(F"Find the first illegal character in each corrupted line of the navigation subsystem. What is the total syntax error score for those errors? {ans}")


ans = []
for line in input:
    ok = True
    stack = []
    for c in line:
        if c in ['(', '[', '{', '<']:
            stack.append(c)
        elif len(stack) > 0 and opp[c] == stack[-1]:
            stack.pop()
        else:
            ok = False
            break

    if ok == True:
        score = 0
        for c in reversed(stack):
            score *= 5
            score += mis[ord[c]]
        ans = [*ans, score]

ans = int(np.median(ans))

print(f"Find the completion string for each incomplete line, score the completion strings, and sort the scores. What is the middle score? {ans}")
