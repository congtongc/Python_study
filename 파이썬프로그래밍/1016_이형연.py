list_1 = [1, 2, 3, 4]
list_파이썬 = ['파이썬', '프로그래밍']
list_a = ['a', 'b', 'c', 'd']

print(list_1)
print(list_파이썬)
print(list_a)
print()
print(type(list_1))
print(type(list_파이썬))
print(type(list_a))

L1 = [] # 빈 리스트
L2 = [2020, 2021, 2022] # 숫자만으로 구성된 리스트
L3 = ['파', '이', '썬', '세', '상', '!']    # 문자열로만 구성된 리스트
L4 = [2020, 3.14, True, '문자열']   # 여러 자료형으로 구성된 리스트
L5 = [L1, L2, L3, L4]
print(L1)
print(L2)
print(L3)
print(L4)
print(L5)
print(L5[2])
print(L2[-2])
print(L4[1:])
print(L4[:-1])
L4[2] = False
print(L4)
print(L2)
L2.append(2023)
print(L2)
L2.clear()
print(L2)
L6 = L2.copy()
print(L6)
L7 = L2
print(L7)
print(L7.count(2023))
# del L7[3]
print(L7)
L2.extend(L3)
print(L2)
print(L2.index('이'))
L2.insert(4, '아')
print(L2)
print(L2.pop(2))
print(L2)
L2.append(2023)
print(L2)
print(L2.remove(2023))
print(L2)
print(L2.index(2023))
L2.reverse()
print(L2)
print(L2.index(2023))
L2.sort()
print(L2)
L2.sort(reverse=True)
print(L2)
# range 함수
a = list(range(10))
print(a)
b = list(range(3,9))
print(b)
c = list(range(-5, 5, 2))
print(c)
d = list(range(10,0,-1))
print(d)
a = list(range(10))
print(a)
print(sum(a))
print(max(a))
print(min(a))
average = sum(a) / len(a)
print(average)
# 리스트의 + 연산
L1 = [2, 5, 7]
L2 = [3, 5, 9]
L3 = L1 + L2
print(L3)
L3 = L2 + L1
print(L3)
L3 += [11, 13]
print(L3)

# 리스트의 * 연산
L1 = [2, 5, 7]
print(L1)
print(L1 * 2)

# 리스트의 비교 연산
L1 = [2, 5, 7]
L2 = [7, 5, 2]
print(L1 == L2)
print(L1 < L2)
print(L1 > L2)