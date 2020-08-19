# https://m.blog.naver.com/PostView.nhn?blogId=zzinuhelios&logNo=120024685950&proxyReferer=https:%2F%2Fwww.google.com%2F
# 대각선이 지나는 단위정사각형 구하는 공식 참고함

from math import gcd


def solution(w,h):
    GCD = gcd(w, h)
    sw = int(w / GCD)
    sh = int(h / GCD)

    mini = sw + sh - gcd(sw, sh)
    answer = w*h - mini*GCD
    return answer


print(solution(8, 12))
print(solution(4, 10))