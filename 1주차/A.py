import sys
input = sys.stdin.readline

t = int(input())
for tc in range(1, t+1):
    a, b, c = map(int, input().split())
    if a < b < c:
        print("STAIR")
    elif a < b >c:
        print("PEAK")
    else:
        print("NONE")