def solution(strings, n):
    return sorted(sorted(strings), key = lambda x : x[n])

print(solution(["sun","bed","car","abce","abcd","cdx"],1))