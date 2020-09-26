def solution(number, k):
    stack = [number[0]]
    for i in number[1:]:
        while len(stack) > 0 and stack[-1] < i and k > 0:
            stack.pop()
            k -= 1
        stack.append(i)
    if k != 0:
        stack = stack[:-k]
    answer = "".join(stack)
    return answer


print(solution("1231234", 3))
# 테스트 12번 해결용
print(solution("319999", 3))