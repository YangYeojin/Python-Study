def solution(s, n):
    answer = ''
    Z, z = ord('Z'), ord('z')

    for i in range(len(s)):
        if s[i] == ' ':
            alphaN = ord(' ')
        elif s[i].isupper():
            alphaN = ord(s[i]) + n
            if Z < alphaN:
                alphaN -= 26
        elif s[i].islower():
            alphaN = ord(s[i]) + n
            if z < alphaN:
                alphaN -= 26
        answer += chr(alphaN)
    return answer

print(solution("ABG X Zz a", 20))