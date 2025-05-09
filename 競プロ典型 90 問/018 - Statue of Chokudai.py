import math
import numpy as np

T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())

for _ in range(Q):
    E = int(input())
    theta = E/T*2*math.pi
    FerrisWheel_x = 0
    FerrisWheel_y = -L/2*math.sin(theta)
    FerrisWheel_z = -L/2*math.cos(theta) + L/2
    #print(FerrisWheel_x, FerrisWheel_y, FerrisWheel_z)
    if FerrisWheel_y == Y:
        distance = X
    elif np.sign(FerrisWheel_y) != np.sign(Y):
        distance = math.sqrt((abs(FerrisWheel_y) + abs(Y))**2 + X**2)
    else:
        distance = math.sqrt(abs(FerrisWheel_y - Y)**2 + X**2)
    #print('distance: '+ str(distance))

    ans = math.degrees(math.atan(FerrisWheel_z / distance))
    print('{:.012f}'.format(ans))