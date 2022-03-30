n, m = map(int, input().split())
# 캐릭터의 x, y 좌표와 방향(0: 북, 1: 동, 2: 남, 3: 서)
x, y, direction = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 방문 정보
visited = [[0] * m for _ in range(n)]
# 초기 위치 방문처리
visited[x][y] = 1

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if visited[nx][ny] == 0 and arr[nx][ny] == 0:
        visited[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn = 0
        continue
    else:
        turn += 1
    if turn == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if arr[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn = 0

print(count)