import sys

def SeatAllocate():
    C, R = map(int, sys.stdin.readline().split())
    K = int(sys.stdin.readline())
    circle = 1

    if K > C * R:
        print(0)
    else:
        for i in range((min(C,R) // 2) + 1):
            if K <= 2*(C+R)-4:
                if K <= R:
                    print(circle, K+circle-1)
                    break
                elif K <= R+C-1:
                    print(K-R+circle, R+circle-1)
                    break
                elif K <= 2*R+C-2:
                    print(C+circle-1, R-(K-R-C+2)+circle)
                    break
                elif K <= 2*(C+R)-4:
                    print(2*(C+R)-3-K+circle, circle)
                    break
            circle += 1
            K -= 2*(C+R)-4
            C -= 2
            R -= 2


SeatAllocate()