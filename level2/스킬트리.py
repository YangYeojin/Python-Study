from collections import deque


def solution(skill, skill_trees):
    answer = len(skill_trees)
    for i in range(len(skill_trees)):
        skill_confirm = deque(list(skill))
        for j in range(len(skill_trees[i])):
            if len(skill_confirm) == 0:
                break
            if skill_trees[i][j] == skill_confirm[0]:
                skill_confirm.popleft()
            if skill_trees[i][j] in skill_confirm:
                answer -= 1
                break
    return answer


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))