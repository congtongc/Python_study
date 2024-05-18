# 평균
N = int(input())
score = list(map(int,input().split()))
M = max(score)
result = 0

for i in score:
    result += i/M*100

print(result/N)