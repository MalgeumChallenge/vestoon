# https://www.acmicpc.net/problem/17103
import sys
import math
input = sys.stdin.readline

isPrime = [True for x in range(1000001)]
isPrime[0] = False
for i in range(2, 1001):
    if not isPrime[i]:
        continue

    for j in range(i+i, 1000001, i):
        isPrime[j] = False

# for i in range(2, 101):
#     if isPrime[i]:
#         print(i, end=' ')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = 0
    for i in range(2, N//2 + 1):
        # print('i', i)
        if isPrime[i] and isPrime[N-i]:
            cnt += 1
    
    print(cnt)
