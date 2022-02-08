"""
How many times does the beam hit the internal surface of the white
cell before exiting?
"""
############################## NOTES ##############################
# Equation of white cell: 4x^2 + y^2 = 100
#
# Split the equation: y1 =  sqrt(100-4x^2)
#                     y2 = -sqrt(100-4x^2)
#
# Derivative of each: y1 = -2/sqrt(25-x^2)
#                   : y2 =  2/sqrt(25-x^2)
#
# Hole that it exits/enters: -0.01 to 0.01 (i.e −0.01 ≤ x ≤ +0.01)
#
# Starting point: (0.0, 10.1)
# First impact  : (1.4, -9.6)
#
# Angle of incidence equals angle of reflection
#
# The slope m of the tangent line at any point (x,y)
# of the given ellipse is: m = −4x/y
#
from math import sqrt

# Slope of tangent of white cell, at x,y
slope_tan = lambda x, y: -4*x/y

# Slope of line from point a to point b (x1, y1) = first point (eg. (0,10.1))
slope_lin = lambda xb, xn, yb, yn: (yn-yb)/(xn-xb)

# Angle of incidence
def angle(M1, M2):
    return ((2 * M1) + (M2 * pow(M1, 2)) - M2) / (2 * M1 * M2 - pow(M1, 2) + 1)

def next_point(xn, yn, xb, yb):
    mt = slope_tan(xn, yn)
    ml = slope_lin(xb, xn, yb, yn)
    ang = angle(mt, ml)

    new_m = ang
    new_n = yn - new_m * xn

    intersect1 = (-2*sqrt(25*new_m**2-new_n**2+100)-new_m*new_n)/(new_m**2+4)
    intersect2 = (2*sqrt(25*new_m**2-new_n**2+100)-new_m*new_n)/(new_m**2+4)

    new_x = max([intersect1, intersect2], key=lambda x:abs(x-xn))
    new_y = new_m*new_x + new_n

    return new_x, new_y


xb = 0
yb = 10.1

xn = 1.4
yn = -9.6

result = 0

while not ((-0.01 < xn < 0.01) and (yn > 0)):
    xt, yt = xn, yn
    xn, yn = next_point(xn, yn, xb, yb)
    xb, yb = xt, yt
    result += 1
    #print(xn, yn)

print(result)
