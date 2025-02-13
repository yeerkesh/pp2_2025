import math

def degree_to_radian(degree):
    return degree * (math.pi / 180)

degree = float(input("Input degree: "))
print("Output radian:", degree_to_radian(degree))
