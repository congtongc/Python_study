n = int(input())    # 공간의 크기
x, y = 1, 1        # 시작 좌표
plans = input().split()   # 이동 계획

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]  # 행
dy = [-1, 1, 0, 0]  # 열
move_types = ['L', 'R', 'U', 'D']   # 이동 방향

# 이동 계획을 하나씩 확인
for plan in plans:  # plans = ['R', 'R', 'R', 'U', 'D', 'D']
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):    
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:   # nx, ny가 1보다 작거나 n보다 크면
        continue        # 무시하고 다음 계획으로 넘어감
    # 이동 수행
    x, y = nx, ny

print(x, y)         # 최종 좌표 출력