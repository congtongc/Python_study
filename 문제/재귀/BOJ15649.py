from itertools import permutations

N, M = list(map(int, input().split()))
list_N = [i for i in range(1, N+1)]
permutation_list = list(permutations(list_N, M))

for permutation in permutation_list:
    print(*permutation)