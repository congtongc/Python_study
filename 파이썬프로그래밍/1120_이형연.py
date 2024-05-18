# 8장
import math
print(dir(math))

def factorial(n):

    result = 1
    for i in range(1, n+1):
        result *= i

    return result

print("5! = ", factorial(5))

import math

a = math.factorial(5)
print("5! = ", a)

from math import comb
b = comb(5, 2)
print('5  Combination 2 = ', b)

from math import *
print(pi)

from math import pow, sqrt

a = pow(2,3)
b = sqrt(4)

print('pow(2, 3) = ', a)
print('sqrt(4) = ', b)

from math import pow as p

a = p(2, 3)

print('p(2, 3) = ', a)

from math import pow as p, sqrt as s

a = p(2,3)
b = s(4)

print('p(2, 3) = ', a)
print('s(4) = ', b)

import math

a = math.pow(2, 3)
b = math.sqrt(4)

print('math.pow(2, 3) = ', a)
print('math.sqrt(4) = ', b)
del math
import importlib
import math
importlib.reload(math)
print(dir(math))

import random
print(random.random())
print(random.randint(1, 6))

import random as rd
print(rd.random())
print(rd.randint(1, 6))
print(rd.randrange(1,6))
numlist = [10, 20, 30, 40, 50]
rd.shuffle(numlist)
print(numlist)
print(rd.choice(numlist))
print(rd.sample(numlist, 3))

import sys
print(sys.path)
print('-' * 50)
print(sys.prefix)

import sys
print('-' * 50)
print(sys.version_info)
print('-' * 50)
print(sys.copyright)
print(sys.getwindowsversion())

import os

print(os.getcwd())
print('-' * 50)
print(os.listdir())
print('-' * 50)
print(os.name)

import calendar
print(calendar.monthrange(2020, 12))
print('-' * 20)
print(calendar.weekday(2020, 8, 31))
print('-' * 20)
print(calendar.prmonth(2020, 8))
print('-' * 20)
# print(calendar.prmonth(2020,12))
print(calendar.calendar(2020))

text = '파이썬 프로그래밍!!'
with open('python.txt', 'w') as p:
    p.write(text)

list = ['a', 'b', 'c']
with open('list.txt', 'w') as f:
    f.write(list)

import pickle

list = ['a', 'b', 'c']
with open('list.txt', 'wb') as f:
    pickle.dump(list, f)

import pickle
with open('list.txt', 'rb') as f:
    data = pickle.load()    # 한 줄씩 읽어옴

print(data)

import tempfile

filename = tempfile.mktemp()
print(filename)

import tempfile, os

filename = tempfile.mktemp()
print(filename)

f = tempfile.NamedTemporaryFile(prefix = "mytemp", suffix = "txt", dir = tempfile.gettempdir())
print(f.name)

import mycom

print(mycom.add(3, 5))
print(mycom.sub(3, 5))

import mymod

print('PI = ', mymod.PI)
a = mymod.Circle()
print('반지름이 5일 때 원의 넓이 = ', a.com1(5))


# 9장
file = open("test.txt", "w")
file.write('Hello World!\n파이썬 월드')
file = open("test.txt", "r")
read = file.read()
print(read)
file.close()

file = open("test.txt", "a")
file.write('\n추가 Hello, World!!')
file = open("test.txt", "r")
read = file.read()
print(read)
file.close()

file = open("test.txt", "w")
file.write('파이썬 프로그래밍')
file = open("test.txt", "r")
read = file.read()
print(read)
file.close()

file = open("test1.txt", "x")
file.write('대한민국 만세!!')
file.close()
file = open("test1.txt", "r")
read = file.read()
print(read)
file.close()

with open('test1.txt', 'x') as file:
    file.write('대한민국 만세!!')

with open("test1.txt", "r") as file:
    read = file.read()
    print(read)

f = open("note_two.txt", "w")
msg1 = "Hello World \n"
msg2 = "Welcome to Python \n"
msg3 = "Python is fun \n"
f.write(msg1)
f.write(msg2)
f.write(msg3)
f = open("note_two.txt", "r")
print(f.read())
f.close()

with open("note_two.txt", "w") as f:
    msg1 = "Hello World \n"
    msg2 = "Welcome to Python \n"
    msg3 = "Python is fun \n"
    a = 3000
    b = 60
    c = 100
    f.write(msg1)
    f.write(msg2)
    f.write(msg3)
    # f.write(a)
    f.write(f"{a}\n")
    f.write(f"{b}\n")
    f.write(f"{c}\n")

with open("note_two.txt", "r") as f:
    print(f.read())

with open("note_two.txt", "r") as f:
    for msg in f:
        print(msg)

import csv
listing = (['Malibu', 'Chevrolet', 22965],
['Fusion', 'Ford', 23735],
['Accord','Honda', 24615],
['Sonata', 'Hyundai', 23185],
['Altima', 'Nissan', 24645],
['Camry', 'Toyota', 24765])

with open("car.csv", "w", newline = '') as f:
    car_writer = csv.writer(f)
    car_writer.writerows(listing)

with open("car.csv", "r") as f:
    car_reader = csv.reader(f)
    for row in car_reader:
        names = row[0]
        makers = row[1]
        price = row[2]
        print(names, makers, price)

def divide(x, y):

    try:
        result = x/y
    
    except ZeroDivisionError as zero_div_err:
        print("0으로 나눌 수 없습니다.", zero_div_err)
    
    else:
        print("정상적으로 나눗셈이 실행되었습니다. 결과는 =", result)

    finally:
        print("\n프로그램을 종료합니다.")
    
input_a = int(input('피제수를 입력해 주세요: '))
input_b = int(input('제수를 입력해 주세요: '))
print()
divide(input_a, input_b)

try:
    input_x = int(input('짝수를 입력하세요: '))
    if input_x % 2 != 0:
        raise Exception('짝수가 아닙니다.')
    
    if input_x == 0:
        raise Exception('0을 입력했군요')
    
except Exception as e:
    print('예외가 발생했습니다.', e)

else:
    print('잘했습니다. 입력한 수는 짝수입니다.')

finally:
    print('\n프로그램을 종료합니다.')