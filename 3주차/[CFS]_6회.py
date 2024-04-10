# https://codeforces.com/contest/1955/problem/B
import sys
input = sys.stdin.readline

t = int(input())
for tc in range(1, t+1):
    n, c, d = map(int, input().split())
    elements = list(map(int, input().split()))
    elements.sort()
    a = elements[0]
    correct = []

    for i in range(n):
        for j in range(n):
            correct.append(a + i*c + j*d)
    correct.sort()

    if correct == elements:
        print("YES")
    else:
        print("NO")
