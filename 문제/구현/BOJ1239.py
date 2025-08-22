import itertools

N = int(input())
Dogs = list(map(int, input().split()))
Dogs_comb = itertools.permutations(Dogs, N)