import sys; input = sys.stdin.readline

# 오류 코드
# N = int(input())
# card = []
# for _ in range(N):
#     C = int(input())
#     card.append(C)  # card 리스트에 입력값 저장
# card.sort()         # 리스트 오름차순 정렬

# sum = [0] * N       # 합 배열 지정
# sum[0] = card[0]    # 인덱스 첫번째 값 저장
# for i in range(1, N):
#     sum[i] = sum[i-1] + card[i]     # 누적 합 리스트

# result = 0
# for j in range(1,N):
#     result += sum[j]    # 누적 합 리스트 합

# print(result)

# 정답 코드(힙 큐 사용)
import heapq

N = int(input())
cards = list(int(input()) for _ in range(N))    # 리스트 형태로 입력
heapq.heapify(cards)                            # cards 리스트를 heap 구조로 변경
cnt = 0

while len(cards) > 1:                     # cards 리스트에 카드가 1장이하로 남을 때까지     
    tmp = heapq.heappop(cards) + heapq.heappop(cards)   # cards 힙에서 2개의 수를 뽑아 더함
    heapq.heappush(cards, tmp)                          # cards 힙에 합한 값을 push
    cnt += tmp                                          # 최종 값인 cnt에 합한 값을 더함

print(cnt)