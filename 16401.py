import sys
input = sys.stdin.readline

M, N = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)

def check(k):
    cnt = M
    for cookie in arr:
        if cookie < k:
            return False
        
        cnt -= cookie//k

        if cnt <= 0:
            return True
    
    return False

lo = 1
hi = max(arr)+1
if not check(lo):
    print(0)
    exit()

while lo+1 < hi:
    mid = (lo+hi)//2

    if check(mid):
        lo = mid
    else:
        hi = mid

print(lo)



