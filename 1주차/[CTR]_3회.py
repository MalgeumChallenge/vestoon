import sys
input = sys.stdin.readline


def transform(n): # 2자리수에 맞춰 앞에 0을 붙여주는 함수, 사실 내장함수나 포메팅 옵션이 있는 걸로 알지만 콘테스트 당시에는 몰랐기에...
    n = str(n)
    return n if len(n) == 2 else '0'+n


t = int(input())
for tc in range(1, t+1):
    h, m = map(int, input().split(':'))
    half = "AM" if h < 12 else # "PM"  # AM, PM 을 정하는 기준

    if h == 12 or h == 0:  # 이 두 가지 경우를 제외하면 전부 12로 나눈 나머지를 계산하면 된다
        h = 12
    else:
        h %= 12
    h = transform(h)
    m = transform(m)

    print(h, ':', m, ' ', half, sep='')
