import sys; input = sys.stdin.readline

word = input()
alphabet = {'c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='}

for i in alphabet:
    word = word.replace(i, '$')

word = word.strip()
print(len(word))