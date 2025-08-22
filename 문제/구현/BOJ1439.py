# 기존 상태와 비교하여 변하면 cnt 증가, 0과 1의 경우 중 가장 작은 경우 출력 
S = str(input())
cnt0 = 0
cnt1 = 0
state = ''

for i in S:
    if i == '0' and state != '0':
        cnt0 += 1
        state = '0'
    elif i == '1' and state != '1':
        cnt1 += 1
        state = '1'

print(min(cnt0, cnt1))

# 0과 1의 경우를 따로 정하는 것이 아닌 서로 인접한 같은 수끼리 하나의 그룹으로 생각하여 숫자가 변할 경우 그룹이 변한 걸로 간주하여 cnt 증가 후 2로 나눈 몫 출력(몫이 그룹의 수)
S = str(input())

cnt = 1

for i in range(1, len(S)):
    if S[i - 1] != S[i]:
        cnt += 1
print(cnt // 2)