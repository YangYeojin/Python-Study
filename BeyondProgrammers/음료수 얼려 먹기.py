import sys


def juiceIce():
    # 입력부
    N, M = map(int, sys.stdin.readline().split())
    iceTray = []
    for i in range(N):
        iceTray += list(map(str, sys.stdin.readline().split()))
    iceN = 0    # 완성되는 아이스크림 개수

    # range 오류 귀찮으니까 그냥 1로 패딩
    pIceTray = []
    for i in range(N+2):
        if i == 0 or i == N+1:
            pIceTray += ['1'*(M+2)]
        else:
            pIceTray += ['1'+iceTray[i-1]+'1']
    visit = [[False for col in range(M+2)] for row in range(N+2)]   # 방문 여부 확인하는 테이블도 패딩한 크기로 그림

    # 이동 방향
    dirX = [0, 0, -1, 1]
    dirY = [-1, 1, 0, 0]

    # dfs 함수 : 연결된 칸으로 이동하며 방문을 기록
    def dfs(graph, c, r, visited):
        visited[c][r] = True
        for k in range(4):
            if graph[c+dirX[k]][r+dirY[k]] == '0' and visited[c+dirX[k]][r+dirY[k]] is False:
                dfs(graph, c+dirX[k], r+dirY[k], visited)
        return visited

    # 1,1(패딩 전 0,0)부터 칸을 탐색하며 아이스크림의 개수를 세는 함수
    for i in range(1, len(pIceTray)):
        for j in range(1, len(pIceTray[i])):
            if pIceTray[i][j] == '0' and visit[i][j] is False:
                visit = dfs(pIceTray, i, j, visit)
                iceN += 1

    print(iceN)


juiceIce()