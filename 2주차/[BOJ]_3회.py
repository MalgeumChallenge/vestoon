# https://www.acmicpc.net/problem/16401
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True) # 꺼내기 좋게 역순으로 정렬

def check(k): # 결정함수
    cnt = M
    for cookie in arr:
        if cookie < k: # 정렬되어 있기 때문에 리턴
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



