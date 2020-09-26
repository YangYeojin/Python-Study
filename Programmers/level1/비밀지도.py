def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        map1 = format(arr1[i], 'b')
        if len(map1) != n:
            map1 = '0'*(n-len(map1)) + map1

        map2 = format(arr2[i], 'b')
        if len(map2) != n:
            map2 = '0'*(n-len(map2)) + map2

        wall = ''
        map1 = list(map1)
        map2 = list(map2)

        for j in range(n):
            if int(map1[j]) + int(map2[j]) > 0:
                wall += '#'
            else:
                wall += ' '
        answer.append(wall)
    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
