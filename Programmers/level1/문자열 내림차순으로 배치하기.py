def solution(s):
    answer = ''
    a = []
    a = sorted(s, reverse=1)
    answer = ''.join(a)
    return answer