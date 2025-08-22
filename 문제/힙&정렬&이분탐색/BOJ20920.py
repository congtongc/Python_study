# 마신 맥주 선호도 합 >= 원하는 선호도
# 마신 맥주 수 == 축제 기간
# 내 주량 증가 => 맥주 선택지 & 선호도 합 증가

import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
beers = [tuple(map(int, input().split())) for _ in range(K)]

beers.sort(key = lambda x: (x[1], -x[0]))

# 가능한지 확인
def possible(lev):
    cnt, sum = 0
    for pre, alc in beers:
        if alc <= lev:
            cnt += 1
            sum += pre
            if cnt == N:
                break
    return cnt == N and pre >= M

# 이분 탐색
left, right = 1, beers[-1][1]
result = -1
while left <= right:
    mid = (left + right) // 2
    if possible(mid):
        result = mid
        right = mid - 1
    else:
        left = mid + 1
        
print(result)