n = int(input())    # No of lines
x = 0   # Initial value of x = 0
for _ in range(n):
    statement = input().strip()
    if "+" in statement:
        x += 1
    if "-" in statement:
        x -= 1
print(x)
