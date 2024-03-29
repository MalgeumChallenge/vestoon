import sys
input = sys.stdin.readline

t = int(input())
for tc in range(1, t+1):
    a, b, c = map(int, input().split())
    if a + 1 != c:
        print(-1)
        continue
    if a == 0:
        print(b)
        continue

    cntA = a
    n = 0
    while n+1 <= cntA:
        n += 1
        cntA -= n
    if cntA:
        n += 1
    k = n - cntA
    blank = 2*k -1
    if not cntA:
        blank -= 1
    cntB = b - blank
    # 기본적으로 n-1
    ans = n
    # print('init', ans)

    while cntB > 0:
        ans += 1
        cntB -= n
    print(ans)
