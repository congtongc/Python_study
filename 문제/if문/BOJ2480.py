# 주사위 세개
import sys; input = sys.stdin.readline

dice = list(map(int, input().split()))

if dice[0] == dice[1] == dice[2]:
    print(10000 + dice[0]*1000)
elif dice[0] == dice[1] or dice[1] == dice[2]:
    print(1000 + dice[1] * 100)
elif dice[0] == dice[2]:
    print(1000 + dice[0] * 100)
elif dice[0] != dice[1] != dice[2]:
    max_dice = max(dice)
    print(max_dice * 100)