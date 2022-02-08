"""
Using the numbers 1 to 10, and depending on arrangements,
it is possible to form 16- and 17-digit strings. What is the
maximum 16-digit string for a "magic" 5-gon ring?
"""
#"""
from itertools import permutations

perms = permutations([1,2,3,4,5,6,7,8,9,10])

solutions = []
for p in perms:
    for eq in range(5,30):
        #print(eq)
        a = p[0]
        b = p[1]
        c = p[2]
        d = p[3]
        e = p[4]
        f = p[5]
        g = p[6]
        h = p[7]
        i = p[8]
        j = p[9]
        if a+b+c == eq and d+c+e == eq and f+e+g == eq and h+g+i == eq and j+i+b == eq:
            solution_u = [(a,b,c), (d,c,e), (f,e,g), (h,g,i), (j,i,b)]
            ind = solution_u.index(min(solution_u))
            solution = solution_u[ind:] + solution_u[:ind]
            if solution not in solutions:
                solutions.append(solution)
                print(solution)

solutions_con = []

for solution in solutions:
    s = []
    for ss in solution:
        s.append("".join([str(x) for x in ss]))
    solutions_con.append(int("".join(s)))

print(max([x for x in solutions_con if x < 10**16]))
