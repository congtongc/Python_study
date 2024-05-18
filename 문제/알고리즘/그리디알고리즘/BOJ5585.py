import sys; input = sys.stdin.readline

value = int(input())
count = 0
change = 1000 - value

def money():
    global count, change
    list = [500,100,50,10,5,1]  # 거스름돈 리스트
    # for문을 통해 순차적으로 거스름돈 금액에 맞게 분류
    for i in list:
        if change >= i:
            count += (change//i)
            change %= i
    # 거스름돈 수 반환
    return count

print(money())