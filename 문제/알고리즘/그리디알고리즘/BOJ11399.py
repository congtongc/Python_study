import sys
sys.setrecursionlimit(5000)
# 줄 서 있는 사람의 수
N = int(input('사람 수 : '))
# 각자의 ATM 사용 시간
P = list(map(int , input("시간 : ").split()))
# 최적 시간 순으로 정렬(퀵 정렬)
def qsort(arr, s, e):
    # 마지막 값에 도착할 때까지
    if s < e:
        pivot = arr[s]  # 피봇으로 지정
        bs, be = s, e   
        while s < e:
            while s < e and pivot <= arr[e]:    
                e -= 1
            while s < e and pivot >= arr[s]:
                s += 1
            if s < e:
                arr[s], arr[e] = arr[e], arr[s]
        arr[bs], arr[s] = arr[s], arr[bs]
        # 재귀 함수
        if bs < s:
            qsort(arr, bs, s - 1)
        if be > e:
            qsort(arr, s + 1, be)

# 최적 시간 순으로 정렬(선택 정렬)
def sel_sort(arr):
    for i in range(len(arr)-1):
        min = i
        for j in range(i+1, len(arr)):
            if arr[min] >= arr[j]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]

# 누적 사용 시간 합
def sum_total(arr):
    result = 0
    temp = 0
    # 누적된 시간의 합과 각 사용자의 시간 합
    for number in arr:
        temp += number
        result += temp
    # 총 시간의 합 반환
    return result

# qsort(P, 0, len(P)-1)
# sel_sort(P)
P.sort()    # 파이썬 제공 정렬 함수
print(sum_total(P))