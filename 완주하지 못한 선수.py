import collections as col
def solution(participant, completion):
    answer = list((col.Counter(participant) - col.Counter(completion)).keys())[0]
    # col.Counter : collections 모듈의 Counter()함수에 list를 입력하여 요소의 개수를 Dictionary 형태로 반환함
    # - : 두 Dictionary끼리 감산
    # keys() : 감산된 값의 key{key:value 형식으로 leo : 1과 같이 저장되어 있음}를 추출
    # list[0] : 저장된 값(dictionary의 key 형식)을 list 형식으로 변경
    # answer = : return하기 위해 list를 answer 변수에 저장
    return answer