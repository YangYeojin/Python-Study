def solution(n, lost, reserve):
    no_uni = list(set(lost) - set(reserve))
    reserve = list(set(reserve) - set(lost))
    have_uni = n - len(no_uni)
    for i in range(len(no_uni)):
        if (no_uni[i]-1) in reserve:
            reserve.remove(int(no_uni[i]-1))
            have_uni += 1
        elif (no_uni[i]+1) in reserve:
            reserve.remove(int(no_uni[i]+1))
            have_uni += 1
    return have_uni

print(solution(10, [2,4,10], [2,3,8]))
