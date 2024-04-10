import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())
    ships = list(map(int, input().split()))
    ans = 0
    i = 0
    j = n-1
    while k > 0 and i <= j:
        # print("ij", i, j)
        l, r = ships[i], ships[j]
        if i == j and l <= k:
            ans += 1
            break

        if l < r:
            if k < 2*l - 1:
                break
            ans += 1
            k -= 2*l
            ships[j] -= l
            i += 1
        elif l > r:
            if k < 2*r:
                break
            ans += 1
            k -= 2*r
            ships[i] -= r
            j -= 1
        else:
            if k < l*2 - 1:
                break
            i += 1
            if k == 2*l - 1:
                ans += 1
            else:
                ans += 2
                j -= 1
            k -= 2 * l


    print(ans)


