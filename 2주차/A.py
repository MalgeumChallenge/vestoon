import sys
input = sys.stdin.readline

t = int(input())
for tc in range(1, t+1):
    n, a, b = map(int, input().split())
    if a*2 <= b:
        print(n*a)
        continue

    dp = [0 for x in range(n+1)]
    dp[1] = a
    for i in range(2, n+1):
        dp[i] = min(dp[i-1]+a, dp[i-2]+b)

    print(dp[n])