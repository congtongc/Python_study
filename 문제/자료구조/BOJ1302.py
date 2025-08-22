N = int(input())
book = {}

for i in range(N):
    title = input()
    if title in book:
        book[title] += 1
    else:
        book[title] = 1
        
max_value = max(book.values())

best_seller = [title for title, number in book.items() if number == max_value]

print(sorted(best_seller)[0])