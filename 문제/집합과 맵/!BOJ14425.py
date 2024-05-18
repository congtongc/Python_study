import sys; input = sys.stdin.readline

# 시간 초과 에러
# N, M = list(map(int,input().split()))
# S = list()
# L = list()
# count = 0
# # 입력 받고 넣기
# for i in range(N):
#     A = input().split()
#     S.append(A)
# # 입력 받고 넣기
# for j in range(M):
#     B = input().split()
#     L.append(B)
# # 비교하여 count+1
# for h in range(len(S)):
#     for k in range(len(L)):
#         if (S[h] == L[k]):
#             count += 1
# print(count)

# 최적화 후
# 입력 받기
# N, M = list(map(int, input().split()))
# S = [tuple(input().split()) for _ in range(N)]
# L = [tuple(input().split()) for _ in range(M)]

# # 배열 비교
# S = set(S)
# L = set(L)
# count = len(S & L)

# # 출력
# print(count)

# 오류 해결
N, M = map(int,input().split())
strings = {input().rstrip() for _ in range(N)}
cnt = 0

for i in range(M):
    string = input().rstrip()
    if string in strings:
        cnt += 1

print(cnt)