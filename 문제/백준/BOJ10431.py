import sys; input = sys.stdin.readline

P = int(input())
for _ in range(P):
    cnt = 0
    T, *num = list(map(int,input().split()))
    for i in range(len(num)):
        for j in range(i+1, len(num)):
            if num[i] > num[j]:
                cnt += 1 
    print(f"{T} {cnt}")