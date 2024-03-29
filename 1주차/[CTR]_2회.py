import sys
input = sys.stdin.readline

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    x = "##"
    y = ".."
    line1 = '' # #먼저 시작하는 줄
    line2 = '' # .먼저 시작하는 줄
    for i in range(n//2):
        line1 += x+y
        line2 += y+x
    if n%2: # 홀수인 경우 하나 추가
        line1 += x
        line2 += y

    for j in range(n//2): # 행 길이만큼 반복
        print(line1)
        print(line1)
        print(line2)
        print(line2)
    if n%2: # 홀수인 경우 하나 추가
        print(line1)
        print(line1)
