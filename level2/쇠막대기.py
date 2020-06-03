def solution(arrangement):
    answer = 0
    Layer = 0
    arr = arrangement.replace("()", "|")

    for i in range(len(arr)):
        if arr[i] == "(":
            Layer += 1
        elif arr[i] == ")":
            Layer -= 1
            answer += 1
        elif arr[i] == "|":
            answer += Layer
    return answer + Layer

print(solution("()(((()())(())()))(())"))