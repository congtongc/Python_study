# 나머지
arr = []
for i in range(10):
    N = int(input())
    arr.append(N%42)
arr = set(arr)      # set 함수 : 중복이 없는 집합
print(len(arr))     