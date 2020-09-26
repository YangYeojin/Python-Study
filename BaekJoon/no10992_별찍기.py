import sys


def star():
    S = int(sys.stdin.readline())

    for i in range(S):
        if i > 0 and i < S-1:
            line = ''.join([" "*(S-i-1), "*", " "*(i*2-1), "*"])
        else:
            line = ''.join([" "*(S-i-1), "*"*((i+1)*2-1)])
        print(line)


star()