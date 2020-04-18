'''
def solution(answers):
    winner = []
    person1_answer_pattern = [1, 2, 3, 4, 5]
    person2_answer_pattern = [2, 1, 2, 3, 2, 4, 2, 5]
    person3_answer_pattern = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    person1_score = 0
    person2_score = 0
    person3_score = 0

    # 수포자와 답안의 비교를 원활히 하기 위해 수포자의 답지패턴 길이를 문제 수보다 조금 길게 조정함
    person1_answer_pattern *= (len(answers) // len(person1_answer_pattern) + 1)
    person2_answer_pattern *= (len(answers) // len(person2_answer_pattern) + 1)
    person3_answer_pattern *= (len(answers) // len(person3_answer_pattern) + 1)

    # 답안과 각 사람의 답지를 비교하여 점수매기는 과정
    for i in range(len(answers)):
        if answers[i] == person1_answer_pattern[i]:
            person1_score += 1
        if answers[i] == person2_answer_pattern[i]:
            person2_score += 1
        if answers[i] == person3_answer_pattern[i]:
            person3_score += 1
    print(person1_score, person2_score, person3_score)

    # 1위를 가려내는 과정
    if person1_score >= person2_score and person1_score >= person3_score:
        winner = [1]
        if person1_score == person2_score:
            winner.append(2)
        if person1_score == person2_score:
            winner.append(3)
    elif person2_score >= person3_score:
        winner = [2]
        if person2_score == person3_score:
            winner.append(3)
    else:
        winner = [3]

    return winner
# 테스트 2, 10, 12 실패
'''

def solution(answers):
    winner = []
    person1_answer_pattern = [1, 2, 3, 4, 5]
    person2_answer_pattern = [2, 1, 2, 3, 2, 4, 2, 5]
    person3_answer_pattern = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]

    # 수포자와 답안의 비교를 원활히 하기 위해 수포자의 답지패턴 길이를 문제 수보다 조금 길게 조정함
    person1_answer_pattern *= (len(answers) // len(person1_answer_pattern) + 1)
    person2_answer_pattern *= (len(answers) // len(person2_answer_pattern) + 1)
    person3_answer_pattern *= (len(answers) // len(person3_answer_pattern) + 1)

    # 답안과 각 사람의 답지를 비교하여 점수매기는 과정
    for i in range(len(answers)):
        if answers[i] == person1_answer_pattern[i]:
            score[0] += 1
        if answers[i] == person2_answer_pattern[i]:
            score[1] += 1
        if answers[i] == person3_answer_pattern[i]:
            score[2] += 1

    # 1위를 가려내는 과정
    max_score = max(score)
    print("score : ", score)
    print("max : ", max_score)
    for i in range(3):
        if score[i] == max_score:
            winner.append(i+1)
    return winner
