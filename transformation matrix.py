import math
import numpy as np

def createIFS (scalar, theta):

    transMatrix = [
        [scalar * (math.cos(theta)), -1 * scalar * math.sin(theta)],
        [scalar * (math.sin(theta)), scalar * (math.cos(theta))]
        ]
    flattened_result = " ".join(f"{item:.4f}" for sublist in transMatrix for item in sublist)
    return flattened_result
        
# def createParamEquation (x, y, t):
#     pointarray = [x, y]
#     point = (x + (t * (y-x)))
#     return 

# def createTransVector(x, y, t):



# angles for the pentagon
angle_pentagon = [-108, -36, 36, 108, 180]

# translation vectors for t bhe pentagon
transVec_pentagon = [
    "1.206 0.633 0.2",
    "0.77 1.343 0.2",
    "-0.04 1.146 0.2",
    "-0.103 0.316 0.2",
    "0.666 0.000 0.2"
]

# angles for the rhombus
angle_rhombus = [-90, 0, 90]

# translation vectors for the rhombus
transVec_rhombus = [
    "0.5 0.5 0.33",
    "0 1 0.33",
    "-0.5 0.5 0.33"
]

# angles for the octagon
angle_octagon = [-135, -90, -45, 0, 45, 90, 135, 180 ]



# translation vectors for the octagon
transVec_octagon = [
    
    "1.4714 0.4714 0.1",
    "1.7071 1.3737 0.1",
    "1.2357 2.1785 0.1",
    "0.333 2.4142 0.1",
    "-0.4714 1.9428 0.1",
    "-0.707 1.0404 0.1",
    "-0.2357 0.2357 0.1",
    "0.666 0 0.1"
]

# angles for the irr_octagon_1
angle_octagon1 = [-90, 0, 90, 180]



# translation vectors for the irr_octagon_1
transVec_octagon1 = [
    
    "6 3.66  0.1",
    "2.333 8 0.1",
    "-2 4.333 0.1",
    "1.66 0 0.1"
]

s1 = 1/4

# angles for the irr_octagon_2
angle_octagon2 = [-135, -45, 45, 135 ]



# translation vectors for the irr_octagon_2
transVec_octagon2 = [
    "4.8333 0.833  0.1",
    "5.1666 6.833 0.1",
    "-0.833 7.166 0.1",
    " -1.166 1.166  0.1"
]
s2 = math.sqrt(2)/8

for n, (i, vec) in enumerate(zip(angle_octagon2, transVec_octagon2), start=1):
    result = createIFS(1, math.radians(i))
    print(result, vec)


