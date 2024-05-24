import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
NGE = [0 for x in range(N)]           
st = deque()

for i in range(N-1, -1, -1):

    while st:
        cmp = st.popleft()

        if arr[i] < cmp:
            st.appendleft(cmp)
            st.appendleft(arr[i])
            NGE[i] = cmp
            break
    else:
        NGE[i] = -1
        st.appendleft(arr[i])


print(*NGE)


# 오른쪽에 있는 수 중 자기보다 크면서 가장 가까운거
    
