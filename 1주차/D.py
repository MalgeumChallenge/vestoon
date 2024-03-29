import sys
input = sys.stdin.readline


def isDeci(n): # 여기도 문자열로 받는다
    for x in n:
        if x != '0' and x != '1':
            return False
    return True


def check(n):  # n 은 문자열로 들어온다
    if isDeci(n):
        return True
    l = len(n)
    n = int(n)

    ub = 2 ** l
    for x in range(2, ub):
        l = int(str(bin(x))[2:])
        if n%l == 0:
            r = n//l
            if check(str(r)):
                return True

    return False


t = int(input())
for tc in range(1, t+1):
    n = input().rstrip()
    # print('test', n)
    print("YES" if check(n) else "NO")