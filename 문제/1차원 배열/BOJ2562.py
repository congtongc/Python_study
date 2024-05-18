# 최댓값
max = 0
num = 0
for i in range(1,10):
    n = int(input())
    if n>max:
        max = n
        num = i

print('%d\n%d' %(max,num))