no_of_problems = int(input())
no_of_problems_solved = 0
for _ in range(no_of_problems):
    decision = sum(list(map(int,input().split())))
    if decision >= 2:
        no_of_problems_solved  += 1
print(no_of_problems_solved)