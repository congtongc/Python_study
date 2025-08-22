N = int(input())
coin = []
delivery_fee = []
for i in range(N):
    max_coin, delivery = map(int, input().split())
    coin.append(max_coin)
    delivery_fee.append(delivery)

coins = sorted(set(coin))

bestfit = 0
result = 0
for i in coins:
    price = 0
    for j in range(N):
        if i<= coin[j] and i>delivery_fee[j]:
            price += i - delivery_fee[j]

    if bestfit < price:
        bestfit = price
        result = i

print(result)