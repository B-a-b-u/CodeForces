n , k = map(int,input().split())
scores = list(map(int,input().split()))
next_round = 0
for i in range(n):
    if scores[i] >= scores[k-1] and scores[i] > 0:
        next_round += 1
print(next_round)