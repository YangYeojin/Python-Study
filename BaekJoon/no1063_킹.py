import sys

def king():
    # 입력부
    K, S, N = map(str, sys.stdin.readline().split())
    kx, ky = ord(K[0]) - 64, int(K[1])
    sx, sy = ord(S[0]) - 64, int(S[1])
    N = int(N)
    Mv = list()
    for i in range(N):
        Mv += list(map(str, sys.stdin.readline().split()))

    # 조작부
    def Move(m, x, y):
        if m == 'R' and x+1 <= 8:
            x += 1
        elif m == 'L' and x-1 >= 1:
            x -= 1
        elif m == 'B' and y-1 >= 1:
            y -= 1
        elif m == 'T' and y+1 <= 8:
            y += 1
        elif m == 'RT' and x+1 <= 8 and y+1 <= 8:
            x += 1
            y += 1
        elif m == 'LT' and x-1 >= 1 and y+1 <= 8:
            x -= 1
            y += 1
        elif m == 'RB' and x+1 <= 8 and y-1 >= 1:
            x += 1
            y -= 1
        elif m == 'LB' and x-1 >= 1 and y-1 >= 1:
            x -= 1
            y -= 1
        else:
            x, y = -1, -1
        return [x, y]

    for i in range(len(Mv)):
        tempK = Move(Mv[i], kx, ky)
        if tempK != [-1, -1]:
            if tempK == [sx, sy]:
                tempS = Move(Mv[i], sx, sy)
                if tempS != [-1, -1]:
                    sx, sy = tempS[0], tempS[1]
                    kx, ky = tempK[0], tempK[1]
            else:
                kx, ky = tempK[0], tempK[1]

    # 출력부
    print(''.join([chr(kx+64), str(ky)]))
    print(''.join([chr(sx + 64), str(sy)]))


king()