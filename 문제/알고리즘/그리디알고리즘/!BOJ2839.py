# 무게 입력
N = int(input('무게 : '))
# 봉투의 개수
carry = 0
# 설탕의 무게가 양수일때만 적용
while N >= 0:
    # 먼저 가장 무거운 5kg으로 나누기
    if N % 5 == 0:
        carry += (N//5)
        print(carry)
        break
    # 나머지 3kg으로 나누기
    N -= 3
    carry += 1
    # 그 외의 경우(분류 불가)
    if N<0:
        print('-1')