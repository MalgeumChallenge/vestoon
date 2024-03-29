import sys
input = sys.stdin.readline

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    x = "##"
    y = ".."
    line1 = ''
    line2 = ''
    for i in range(n//2):
        line1 += x+y
        line2 += y+x
    if n%2:
        line1 += x
        line2 += y

    for j in range(n//2):
        print(line1)
        print(line1)
        print(line2)
        print(line2)
    if n%2:
        print(line1)
        print(line1)