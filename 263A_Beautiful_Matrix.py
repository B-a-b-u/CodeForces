# Get 5x5 matrix
matrix = list()
n = 5   # no of row and col (square matrix)
for _ in range(n):
    matrix.append(list(map(int,input().split())))
# print(f"Matrix : ",matrix)

# Find the position of 1
# Linear Search on 2D matrix
ctrl = False    # To get exit from outer loop
for r in range(n):
    for c in range(n):
        if matrix[r][c] == 1:
            ctrl = True
            break
    if ctrl:
        break
# print(f"Index of 1 : {r} {c}")

# Beauty Matrix Position
row = 2
col = 2

# Absolute difference
no_of_moves = abs(row-r) + abs(col - c)
print(no_of_moves)