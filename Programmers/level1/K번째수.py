def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        com_list = commands[i]
        devided_list = array[com_list[0] - 1:com_list[1]]
        devided_list.sort()
        answer.append(devided_list[com_list[2]-1])
    return answer