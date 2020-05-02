# 조합문제 (수학)
# [의상명, 의상종류]가 원소로 들어가는 2차원 배열에서 ㅢ사을 입는 경우의 수 추출하기
# 모든 의상종류는 입거나 안 입을 수 있지만 1가지 이상의 의상은 반드시 입어야 함

# 문제풀이
# 1. 2차원 배열에서 옷의 종류를 받아서 sum(clothes, [])[1::2] 의상 종류의 개수를 구하고 len(set()), 각 의상종류에 대해 의복 개수를 구함 count()
# 2. 모든 의상 종류는 입거나 안입을 수 있으므로 의복 개수에 의상을 입지 않는 경우의 수 1을 추가해 줌
#    for i in range(의상종류의 수): answer *= (의상종류 i의 의상 개수 + 1)
# 3. 의복을 아예 입지 않는 경우의 수를 제거함 answer - 1

from collections import Counter

def solution(clothes):
    answer = 1
    clothes = sum(clothes, [])[1::2]
    category_set = list(set(clothes))
    clothes_for_each_category = Counter(clothes)

    for i in range(len(category_set)):
        answer *= clothes_for_each_category[category_set[i]] + 1
    return answer - 1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"], ["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))