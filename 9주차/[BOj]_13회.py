# https://www.acmicpc.net/problem/31844
import sys
input = sys.stdin.readline

# 1.로봇을 박스에 인접한 곳으로 이동
# 2. 밀어서 옮기기

info = input().rstrip()

rob , box, flag = -1, -1, -1
for i in range(10):
    if info[i] == '#':
        box = i
    elif info[i] == '@':
        rob = i
    elif info[i] == '!':
        flag = i

if (flag < box and rob < box) or ( box < flag and box < rob):
    print(-1)
    exit()

# print(rob, box, flag)
print(abs(rob-box)-1 + abs(box-flag))
