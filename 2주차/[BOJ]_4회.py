# https://www.acmicpc.net/problem/2075
import sys
import heapq
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
for _ in range(N-1):
    arr += list(map(int, input().split()))
    arr.sort()
    arr = arr[N:]

print(arr[0])
# print(arr)
