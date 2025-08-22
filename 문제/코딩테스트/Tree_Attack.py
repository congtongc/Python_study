import sys; input = sys.stdin.readline

# 공격 함수 정의
def attack(field, start_row, end_row):
    for i in range(start_row, end_row + 1):
        if 0 <= i < n:  # 유효한 행인지 확인
            for j in range(m):  # 열 순회
                if field[i][j] == 1:
                    field[i][j] = 0  # 환경 파괴범 제거
                    break  # 한 행에서 하나만 제거

# n * m 격자 크기
n, m = map(int, input().split())

# 격자 초기화 (n x m 크기의 2차원 리스트)
tree = []
for _ in range(n):
    tree.append(list(map(int, input().split())))

# L1과 R1은 첫 번째 공격 범위
L1, R1 = map(int, input().split())
# 밀린 인덱스를 복구하기 위한 -1
L1 -= 1
R1 -= 1

# L2과 R2은 두 번째 공격 범위
L2, R2 = map(int, input().split())
# 밀린 인덱스를 복구하기 위한 -1
L2 -= 1
R2 -= 1

# 첫 번째 범위 공격
attack(tree, L1, R1)

# 두 번째 범위 공격
attack(tree, L2, R2)

# tree 배열 속의 1의 개수 체크(cnt)
cnt = sum(row.count(1) for row in tree)
print(cnt)