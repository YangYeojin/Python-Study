def solution(name):
    answer = 0
    made = list('A'*len(name))
    name = list(name)
    A, Z = ord('A'), ord('Z')
    idx = 0
    move = 0

    while name != made:
        # 다음에 변경할 알파벳의 위치 찾기
        while name[idx+move] == made[idx+move] and name[idx-move] == made[idx-move] and name != made:
            move += 1
            if idx+move == len(name):
                idx -= len(name)
        if name[idx+move] != made[idx+move]:
            idx += move
        else:
            idx -= move
        answer += move
        move = 0

        # 현재 위치의 알파벳 변경
        alphabet = ord(name[idx])
        made[idx] = name[idx]
        if alphabet - A <= Z - alphabet + 1:
            answer += alphabet - A
        else:
            answer += Z - alphabet + 1

    return answer


print(solution("JEROEN")) ## 56
print(solution("JAAAN")) ## 23
print(solution("ABAAAAAAAAABB")) ## 7
print(solution("ABAAABAAAAABB")) ## 14
