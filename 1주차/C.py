import sys
input = sys.stdin.readline


def transform(n):
    n = str(n)
    return n if len(n) == 2 else '0'+n


t = int(input())
for tc in range(1, t+1):
    h, m = map(int, input().split(':'))
    half = "AM" if h < 12 else "PM"

    if h == 12 or h == 0:
        h = 12
    else:
        h %= 12
    h = transform(h)
    m = transform(m)

    print(h, ':', m, ' ', half, sep='')
