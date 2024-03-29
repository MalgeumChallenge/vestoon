import sys
input = sys.stdin.readline


def isDeci(n): # 여기도 문자열로 받는다, binary decimal 이 맞는지 판별
    for x in n:
        if x != '0' and x != '1':
            return False
    return True


def check(n):  # n 은 문자열로 들어온다
    if isDeci(n): # n 자체가 이미 binary decimal 이라면 그냥 리턴
        return True
    l = len(n)
    n = int(n)

    ub = 2 ** l  # n 의 자릿수를 바탕으로 한 upper bound 계산
    for x in range(2, ub):
        l = int(str(bin(x))[2:]) # upper bound 까지 이진수로 변환 후 슬라이싱을 하는 번거로운 방법 사용, 이것도 더 나은 내장함수가 있을지도?
        if n%l == 0: # 나누어 떨어지는 binary decimal 이 존재한다면
            r = n//l
            if check(str(r)): # 나눈 몫이 binary decimal 인지 혹은 binary decimal의 곱으로 나타낼 수 있는지 재귀를 통해 확인
                return True

    return False


t = int(input())
for tc in range(1, t+1):
    n = input().rstrip()
    # print('test', n)
    print("YES" if check(n) else "NO")
