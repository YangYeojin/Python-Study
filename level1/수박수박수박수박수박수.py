def solution(n):
    answer = ''

    while n >= 2 :
        answer += ''.join("수박")
        n = n - 2

    if n == 1:
        answer += ''.join("수")
    return answer

def watermelon(n):
    answer = ''
    water_melon = "수박"
    half_melon = "수"

    while n >= 2 :
        answer += water_melon
        n = n - 2

    if n == 1:
        answer += half_melon
    return answer