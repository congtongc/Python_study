import sys; input = sys.stdin.readline
str = input().split('-')  # -를 기준으로 숫자들을 분류
b = 0                       
for i in str[0].split('+'): # +가 나오기 전까지의 숫자들만 분류
    b += int(i)
for i in str[1:]:       # 분류하고 남은 나머지 숫자들
    new_list = i.split('+') # 리스트에 나머지 숫자들을 +로 분류
    for j in new_list:
        b -= int(j)     # 나머지 숫자들을 뺌
print(b)