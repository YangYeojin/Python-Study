def solution(brown, yellow):
    i = 1
    while True:
        if yellow%i == 0:
            if (i+2)*(yellow/i+2) == brown + yellow:
                return [int(yellow/i+2), i+2]
        i += 1


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))

'''
테스트 1 〉	통과 (0.04ms, 10.6MB)
테스트 2 〉	통과 (0.04ms, 10.6MB)
테스트 3 〉	통과 (0.11ms, 10.7MB)
테스트 4 〉	통과 (0.04ms, 10.6MB)
테스트 5 〉	통과 (0.04ms, 10.7MB)
테스트 6 〉	통과 (0.06ms, 10.6MB)
테스트 7 〉	통과 (0.11ms, 10.7MB)
테스트 8 〉	통과 (0.11ms, 10.7MB)
테스트 9 〉	통과 (0.09ms, 10.7MB)
테스트 10 〉	통과 (0.12ms, 10.6MB)
테스트 11 〉	통과 (0.03ms, 10.8MB)
테스트 12 〉	통과 (0.04ms, 10.7MB)
테스트 13 〉	통과 (0.04ms, 10.7MB)
'''