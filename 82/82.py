"""
Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), 
a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right 
by moving left, right, up, and down.
"""
import heapq

def shortest_path(G, start, end):
   def flatten(L):       # Flatten linked list of form [0,[1,[2,[]]]]
      while len(L) > 0:
         yield L[0]
         L = L[1]

   q = [(131, start, ())]  # Heap of (cost, path_head, path_rest).
   visited = set()       # Visited vertices.
   while True:
      (cost, v1, path) = heapq.heappop(q)
      if v1 not in visited:
         visited.add(v1)
         if v1 == end:
            return list(flatten(path))[::-1] + [v1]
         path = (v1, path)
         for (v2, cost2) in G[v1].items():
            if v2 not in visited:
               heapq.heappush(q, (cost + cost2, v2, path))

grid = []

with open('82.txt', 'r') as f:
    for line in f:
        line = line.strip('\n')
        rowski = [int(x) for x in line.split(",")]
        grid.append(rowski)

list_o_results = []

G = {}

x_lim = 80
y_lim = 80

for y in range(y_lim):
    for x in range(x_lim):
        if (y+1 != y_lim and x+1 != x_lim) and (y-1 > -1) :
            G[str(grid[y][x]) +" - " + str(x) + ", " + str(y)] = {str(grid[y][x+1]) + " - " + str(x+1) + ", " + str(y): grid[y][x+1], \
                                                                  str(grid[y+1][x]) + " - " + str(x) + ", " + str(y+1): grid[y+1][x], \
                                                                  str(grid[y-1][x]) + " - " + str(x) + ", " + str(y-1): grid[y-1][x]}
            continue

        if (y+1 != y_lim and x+1 != x_lim) and (y-1 == -1):
            G[str(grid[y][x]) +" - " + str(x) + ", " + str(y)] = {str(grid[y][x+1]) + " - " + str(x+1) + ", " + str(y): grid[y][x+1], \
                                                                  str(grid[y+1][x]) + " - " + str(x) + ", " + str(y+1): grid[y+1][x]}
            continue

        if (y+1 == y_lim and x+1 != x_lim) and (y-1 > -1):
            G[str(grid[y][x]) +" - " + str(x) + ", " + str(y)] = {str(grid[y][x+1]) + " - " + str(x+1) + ", " + str(y): grid[y][x+1], \
                                                                  str(grid[y-1][x]) + " - " + str(x) + ", " + str(y-1): grid[y-1][x]}
            continue

        if (y+1 != y_lim and x+1 == x_lim) and (y-1 > -1) :
            G[str(grid[y][x]) +" - " + str(x) + ", " + str(y)] = {str(grid[y+1][x]) + " - " + str(x) + ", " + str(y+1): grid[y+1][x], \
                                                                  str(grid[y-1][x]) + " - " + str(x) + ", " + str(y-1): grid[y-1][x]}
            continue

        if (y+1 != y_lim and x+1 != x_lim) and (y-1 == -1):
            G[str(grid[y][x]) +" - " + str(x) + ", " + str(y)] = {str(grid[y][x+1]) + " - " + str(x+1) + ", " + str(y): grid[y][x+1], \
                                                                  str(grid[y+1][x]) + " - " + str(x) + ", " + str(y+1): grid[y+1][x]}
            continue

        if (y+1 != y_lim and x+1 == x_lim) and (y-1 == -1) :
            G[str(grid[y][x]) +" - " + str(x) + ", " + str(y)] = {str(grid[y+1][x]) + " - " + str(x) + ", " + str(y+1): grid[y+1][x]}
            continue

        if (y+1 == y_lim and x+1 == x_lim) and (y-1 > -1 ) :
            G[str(grid[y][x]) +" - " + str(x) + ", " + str(y)] = {}
            continue

for s in range(80):
    for e in range(80):
        short_path = shortest_path(G, str(grid[s][0]) + " - " + str(0) + ", " + str(s), str(grid[e][79]) + " - " + str(79) + ", " + str(e))

        result_list = []

        for i in short_path:
            result_list.append(int(i.split(" ")[0]))

        list_o_results.append(sum(result_list))
    print(s)

print(min(list_o_results))

#VEEEEEEEEEEEEEERY slow but i already did the algorithm so this was easier
