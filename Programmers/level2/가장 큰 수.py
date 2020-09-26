'''
import copy

def solution(numbers):
    answer = ''
    # 1. 리스트의 숫자를 문자열로 만든다.
    num_str = list(map(str, numbers))
    # 2. sorted 함수를 사용해 문자열이 된 숫자들을 역순으로 정렬한다.
    # 숫자들이 문자열로 변환되면서 sorted()를 사용하면 숫자의 길이에 상관없이
    # 왼쪽부터 첫번째 자리 숫자가 작은 값부터, 동일하다면 두번째 자리에 글자가 없는 것부터 정렬됨
    # 이를 reverse 하면 [3, 30, 34, 5, 9]가 ['9', '5', '34', '30', '3']로 출력됨
    num_str.sort(reverse=True)
    print('num_str:', num_str)
    # 왠진 모르겠지만 그냥 쓰면 숫자를 오른쪽부터 읽어서 numbers에 num_str의 값만을 완전히 복사함
    numbers = copy.deepcopy(num_str)
    # 3. 숫자 i와 i*10 또는 i*100인 숫자가 리스트에 동시에 존재할 때 그 위치를 바꾸어 줌
    for i in range(1, len(num_str)):
        if int(numbers[i])*10 == int(numbers[i-1]):
            numbers[i-1], numbers[i] = numbers[i], numbers[i-1]
            print(numbers)
        if int(numbers[i])*100 == int(numbers[i-1]):
            numbers[i-1], numbers[i] = numbers[i], numbers[i-1]
            print(numbers)
    # 3. 리스트 안의 문자열들을 조인하면 완성!
    answer = "".join(numbers)
    return answer
# 모르겠고 굉장히 많은 오류
'''

def solution(numbers):
    numbers = list(map(str, numbers))
    # sorting 할 때 key 값을 기준으로 정렬
    # key 파라미터의 값은 하나의 인자를 받아 정렬 목적을 위한 키를 리턴하는 함수
    numbers.sort(key=lambda x: x * 3, reverse=True)
    if sum(list(map(int, numbers))) == 0:
        numbers = list(set(numbers))
    return ''.join(numbers)

# 람다 표현식 사용하기 : https://dojang.io/mod/page/view.php?id=2359