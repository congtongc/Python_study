import sys; input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

sum = 0
for _ in range(N):
    # A의 최소값과 B의 최대값을 점차 소거해 나가며 빼낸다.
    sum += A.pop(A.index(min(A))) * B.pop(B.index(max(B))) 
print(sum)