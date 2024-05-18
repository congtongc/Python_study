import sys; input = sys.stdin.readline

N = int(input())
list = [] * N
for _ in range(N):
    Alpha = input()
    A = Alpha.replace("\n", "") 
    list.append(A)
print(list)      # 리스트 문자 확인 코드

num = []
for i in range(len(list)):
    for j in range