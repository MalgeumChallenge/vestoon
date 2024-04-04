# https://www.acmicpc.net/problem/21599
import sys
import heapq
input = sys.stdin.readline

# 그냥 내림차순으로 중복이 최대가 되도록 정렬한 후 선형으로 탐색하면서 강화되는 아이템의 수를 갱신하면 되는 문제
N = int(input())
items = list(map(int, input().split()))
items.sort(reverse=True)
j = -1
for i in range(N):
    if items[i] == 0:
        break
    
    j = max(j, i-1 + items[i])

j = min(j, N-1)

print(j+1)
