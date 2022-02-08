"""
Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text file 
containing the co-ordinates of one thousand "random" triangles, find the number 
of triangles for which the interior contains the origin.
"""
def contain_origin(t):
    p0x, p1x, p2x = t[0], t[2], t[4]
    p0y, p1y, p2y = t[1], t[3], t[5]

    area = 0.5 *(-p1y*p2x + p0y*(-p1x + p2x) + p0x*(p1y - p2y) + p1x*p2y)

    n = 1/(2*area)*(p0y*p2x - p0x*p2y)
    m = 1/(2*area)*(p0x*p1y - p0y*p1x)

    if n > 0 and m > 0 and 1-n-m > 0:
        return True
    return False

result = 0

with open("102.txt") as f:
    for l in f:
        t = [int(x) for x in l.strip("\n").split(",")]
        if contain_origin(t):
            result += 1

print(result)

#could also use herons formula.