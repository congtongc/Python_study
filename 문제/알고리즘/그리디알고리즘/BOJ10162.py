import sys; input = sys.stdin.readline
A = 300
B = 60
C = 10
At = 0
Bt = 0
Ct = 0
T = int(input())
if T % 10 != 0:
    print(-1)
elif T % 10 == 0:
    if T % A and T / A > 0:
        At = T / A
        T %= A
        if T % B and T / B > 0:
            Bt = T / B
            T %= B
            if T % C and T / C > 0:
                Ct = T / C
    elif T % B and T / B > 0:
        Bt = T / B
        T %= B
        if T % C and T / C > 0:
            Ct = T / C
    elif T % C and T / C > 0:
        Ct = T / C
    print(f'{At} {Bt} {Ct}')