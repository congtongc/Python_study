S = list(map(str, input().split()))
T = list(map(str, input().split()))

res = 0
while T:
    T.pop(0)
    if T == S:
        res = 1
    elif len(T) < len(S):
        break
    if T[-1] == 'A':
        T.pop()
    else:
        T.pop()
        T = T[::-1]
    
print(res)