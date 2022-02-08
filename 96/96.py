"""
The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'),
contains fifty different Su Doku puzzles ranging in difficulty, but all
with unique solutions (the first puzzle in the file is the example above).

By solving all fifty puzzles find the sum of the 3-digit numbers found in
the top left corner of each solution grid; for example, 483 is the 3-digit
number found in the top left corner of the solution grid above.
"""

def end(sudoku):
    for s in sudoku:
        for l in s:
            if l == "0":
                return False
    return True

def strip_n(sudoku):
    sudoku_n = []
    for row in sudoku:
        row_n = []
        for pos in row:
            row_n.append(pos[0])
        sudoku_n.append(row_n)
    return sudoku_n


def valid(sudoku):
    sudoku = strip_n(sudoku)
    #print(sudoku)

    # check horisontal
    for s in sudoku:
        s = [x for x in s if x != "0"]
        if len(set(s)) != len(s):
            return False

    # check vertical
    sudoku_ver = []
    for c in range(len(sudoku)):
        cal = []
        for row in sudoku:
            cal.append(row[c])
        sudoku_ver.append(cal)
    for s in sudoku_ver:
        s = [x for x in s if x != "0"]
        if len(set(s)) != len(s):
            return False

    # check square
    sudoku_sq = []
    s_1 = []
    s_2 = []
    s_3 = []
    s_4 = []
    s_5 = []
    s_6 = []
    s_7 = []
    s_8 = []
    s_9 = []
    for sq in range(len(sudoku)):
        if sq < 3:
            n = 0
            for l in sudoku[sq]:
                if n < 3:
                    s_1.append(l)
                elif 2 < n < 6:
                    s_2.append(l)
                elif 5 < n < 9:
                    s_3.append(l)
                n += 1
        elif 2 < sq < 6:
            n = 0
            for l in sudoku[sq]:
                if n < 3:
                    s_4.append(l)
                elif 2 < n < 6:
                    s_5.append(l)
                elif 5 < n < 9:
                    s_6.append(l)
                n += 1
        elif 6 < sq < 9:
            n = 0
            for l in sudoku[sq]:
                if n < 3:
                    s_7.append(l)
                elif 2 < n < 6:
                    s_8.append(l)
                elif 5 < n < 9:
                    s_9.append(l)
                n += 1
    sudoku_sq.append(s_1)
    sudoku_sq.append(s_2)
    sudoku_sq.append(s_3)
    sudoku_sq.append(s_4)
    sudoku_sq.append(s_5)
    sudoku_sq.append(s_6)
    sudoku_sq.append(s_7)
    sudoku_sq.append(s_8)
    sudoku_sq.append(s_9)
    for s in sudoku_sq:
        s = [x for x in s if x != "0"]
        if len(set(s)) != len(s):
            return False

    return True

def backtrack(sudoku, row, pos, first):
    if end(sudoku) and valid(sudoku): 
        return int(sudoku[0][0][0] + sudoku[0][1][0] + sudoku[0][2][0])
    elif end(sudoku):
        return False

    if "n" not in sudoku[row][pos] and sudoku[row][pos] != "0":
        if first:
            if pos == 8:
                if valid(sudoku) and backtrack(sudoku, row+1, 0, True):
                    if end(sudoku):
                        return int(sudoku[0][0][0] + sudoku[0][1][0] + sudoku[0][2][0])
                    else:
                        return True
            else:
                if valid(sudoku) and backtrack(sudoku, row, pos+1, True):
                    if end(sudoku):
                        return int(sudoku[0][0][0] + sudoku[0][1][0] + sudoku[0][2][0])
                    else:
                        return True
        else:
            if pos == 8:
                if valid(sudoku) and backtrack(sudoku, row+1, 0, False):
                    if end(sudoku):
                        return int(sudoku[0][0][0] + sudoku[0][1][0] + sudoku[0][2][0])
                    else:
                        return True
            else:
                if valid(sudoku) and backtrack(sudoku, row, pos+1, False):
                    if end(sudoku):
                        return int(sudoku[0][0][0] + sudoku[0][1][0] + sudoku[0][2][0])
                    else:
                        return True
    else:
        for x in range(1, 10):
            sudoku[row][pos] = str(x) + "n"
            if pos == 8:
                if valid(sudoku) and backtrack(sudoku, row+1, 0, False):
                    if end(sudoku):
                        return int(sudoku[0][0][0] + sudoku[0][1][0] + sudoku[0][2][0])
                    else:
                        return True
            else:
                if valid(sudoku) and backtrack(sudoku, row, pos+1, False):
                    if end(sudoku):
                        return int(sudoku[0][0][0] + sudoku[0][1][0] + sudoku[0][2][0])
                    else:
                        return True

        sudoku[row][pos] = "0"

    return False

sudokus = []

result = 0

with open('sudoku.txt', 'r') as f:
    each = []
    e = True
    for line in f:
        rowski = list(line.strip('\n'))
        if e:
            e = False
            continue
        if rowski[0][0] == 'G':
            sudokus.append(each)
            each = []
            continue

        each.append(rowski)
    sudokus.append(each)


for sudoku in sudokus:
    result += backtrack(sudoku, 0, 0, True)

print(result)

# Takes around 400 seconds :(
