# https://school.programmers.co.kr/learn/courses/30/lessons/1844
from collections import deque


def solution(maps):
    m = len(maps[0])  # map 가로크기
    n = len(maps)  # map 세로크기

    maps[n-1][m-1] = -1  # 마지막 위치 -1 로 설정

    x, y = 0, 0  # 초기 위치

    # 상하좌우 표시
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((x, y))
    # 큐가 빌때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 공간을 벗어나면 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 벽인경우 무시
            if maps[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우만 최단 거리 기록
            if maps[nx][ny] == 1 or maps[nx][ny] == -1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단거리 반환
    return maps[n - 1][m - 1]


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
