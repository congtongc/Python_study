N,K = map(int, input().split())
coins = list()
for i in range(N):
    coins.append(int(input()))   # 각 줄마다 입력받고 리스트에 입력
count = 0

for i in reversed(range(N)):
    count += K//coins[i]    # 화폐의 금액으로 나눈 몫
    K %= coins[i]           # 나누고 남은 나머지

print(count)

# # 최대부터 시작
# for i in range(N - 1, -1, -1):        # -> 역방향 루프문을 사용할 경우 코드가 어려워져 시간 오래걸림 => reversed() 사용
#     # 화폐의 가치보다 금액이 클 경우
#     while K >= coins[i]:
#         count += 1      # 해당 화폐 적용
#         K -= coins[i]   # 화폐의 금액만큼 차감

# print(count)