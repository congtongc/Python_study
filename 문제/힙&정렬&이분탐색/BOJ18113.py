# N(김밥의 개수), K(꼬다리의 길이), M(김밥조각의 최소 개수), L(김밥의 길이)
# (1 ≤ N ≤ 10^6, 1 ≤ K, M ≤ 10^9, N, K, M은 정수), (1 ≤ L ≤ 10^9, L은 정수)
# P의 최대 값, 없으면 -1 출력
# 조각의 길이(P)가 늘어나면 조각의 개수(M)은 줄어들고, 조각의 길이(P)가 줄어들면 조각의 개수(M)은 늘어난다. (조각이 커지면 불가할 가능성이 증가하므로, 이분 탐색을 이용하여 최대값을 찾는다.) 
# 이분 탐색, l과 r을 [(닫힌구간과), )열린구간으로 설정 => [l, r)로 설정
# 이 문제의 경우 [0, 10^9)로 설정
import sys
input = sys.stdin.readline

N, K, M = map(int, input().split())
L = list(int(input()))

for _ in range(N):
    if L < K:
        L = 0
    elif L < 2*K:
        L -= K
    else:
        L -= 2*K 
    
sorted_lengths = sorted(L, reverse=True)