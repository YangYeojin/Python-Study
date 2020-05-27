def solution(arr1, arr2):
    return [[a+b for a, b in zip(a1, a2)] for a1, a2 in zip(arr1, arr2)]

# 바깥쪽 리스트에 있는 for:문이 한 번 돌면 arr1, arr2에서 첫번째 요소를 추출함 ex)[1, 2] [3, 4]
# 안쪽 리스트에서 두 요소(바깥 리스트에서 만들어진 리스트)의 같은 위치에 있는 각 요소를 더한 새로운 리스트를 생성
# 바깥쪽 for:문이 끝날 때까지 반복하면 새로운 리스트가 append 같은 형식으로 계속 붙을 것

print(solution([[1,2],[2,3]], [[3,4],[5,6]]))