import numpy as np

# fetch input manually
inputx = [282, 314]
inputy = [-80, -45]


ans = 0
ext = np.abs(inputy[0])
ans = 0.5*ext*(ext - 1)

print(f"Find the initial velocity that causes the probe to reach the highest y position and still eventually be within the target area after any step. What is the highest y position it reaches on this trajectory? {ans}")


ans = 0
for vx_ in range(0, 400):
    for vy_ in range(-800, 800):
        px, py, vx, vy = 0, 0, vx_, vy_
        while 1:
            px += vx
            py += vy
            vx -= np.sign(vx) if vx != 0 else 0
            vy -= 1

            if inputx[0] <= px and px <= inputx[1] and inputy[0] <= py and py <= inputy[1]:
                ans += 1
                break

            if px > inputx[1] or py < inputy[0]:
                break

print(f"How many distinct initial velocity values cause the probe to be within the target area after any step? {ans}")
