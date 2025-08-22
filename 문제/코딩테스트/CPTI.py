import sys;

input = sys.stdin.readline

# 사람의 수 N, CPTI의 길이 M
N, M = map(int, input().split())
# 길이 N만큼 입력(0,1)
CPTI = []
for _ in range(N):
    CPTI.append(list(map(int, input().split())))
# friend는 친밀한 유형의 수
friend = 0
# zip 함수를 사용하여 for문으로 순환하며 2개의 항을 비교하고 해당하는 값을 합산
for i in range(N):
    current = CPTI[i]  # 현재 순번의 항
    next = CPTI[(i + 1) % N]  # 다음 순번의 항(순환 형태로 하여 마지막 항은 첫째 항과 비교)
    print(f"current: {current}, next: {next}")
# 다른 수 계산
cnt = sum(1 for j, k in zip(current, next) if j != k)
print(f"cnt: {cnt}")

# 다른 수 2개 이하인 경우만 합
if cnt <= 2:
    friend += 1
    print(f"friend: {friend}")

print(friend)
