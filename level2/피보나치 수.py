def solution(n):
    domain = [1, 0]
    if n == 1:
        return 1
    i = 2
    while True:
        if i == n:
            return (domain[0] + domain[1]) % 1234567
        else:
            domain = [domain[0] + domain[1], domain[0]]
            i += 1