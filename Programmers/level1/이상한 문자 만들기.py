def solution(s):
    answer = ''
    sentence, word = 0, 0
    A, a = ord('A'), ord('a')
    cal = a-A
    while sentence != len(s):
        if s[sentence] == ' ':
            answer += s[sentence]
            word = 0
        elif word == 0 or word % 2 == 0:
            word += 1
            if ord(s[sentence]) >= a:
                answer += chr(ord(s[sentence]) - cal)
            else:
                answer += s[sentence]
        else:
            word += 1
            if ord(s[sentence]) < a:
                answer += chr(ord(s[sentence]) + cal)
            else:
                answer += s[sentence]
        sentence += 1
    return answer

print(solution("try hello world"))