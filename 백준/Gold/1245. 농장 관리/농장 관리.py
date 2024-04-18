import sys
from collections import deque

input = sys.stdin.readline

# 입력: 행렬의 크기 n과 m
n, m = map(int, input().split())

# 행렬 데이터 입력받기
data = [list(map(int, input().split())) for _ in range(n)]

# 방향 벡터: 상, 상우, 우, 하우, 하, 하좌, 좌, 상좌
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

# 처리된 인덱스를 저장할 리스트
processed_indices = []

# 너비 우선 탐색 (BFS) 함수 정의
def bfs(start_x, start_y, processed_indices):
    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = True
    component = [(start_x, start_y)]
    while queue:
        x, y = queue.popleft()
        for direction in range(8):
            nx, ny = x + dx[direction], y + dy[direction]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny]:
                continue
            if data[x][y] < data[nx][ny]:
                return 0  # 더 높은 지점을 만났으므로 현재 지점은 최고점이 아님
            if data[x][y] == data[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))
                component.append((nx, ny))
    processed_indices.extend(component)  # 이 컴포넌트의 모든 점을 처리된 것으로 추가
    return 1

# 최고점 개수 계산
total_peaks = 0
for i in range(n):
    for j in range(m):
        if (i, j) not in processed_indices:
            visited = [[False] * m for _ in range(n)]
            total_peaks += bfs(i, j, processed_indices)

print(total_peaks)