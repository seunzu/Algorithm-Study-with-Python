from collections import deque
#n,m입력
n,m=map(int,input().split())

#2차원 리스트 맵 정보 
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

#이동할 네 방향 정의 (상하 좌우 )
dx=[-1,1,0,0]
dy=[0,0,-1,1]

#bfs구현 

def bfs(x,y):
    #큐 구현 
    queue=deque()
    queue.append((x,y))
    #큐가 빌때까지 
    while queue:
        x,y=queue.popleft()
        #네 방향으로 위치 학인 
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            #미로 찾기 공간 벗어난 경우 무시 
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if graph[nx][ny]==0:
                continue
            #해당노드 처음 방문할때, 최단거리 기록 
            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))

    #가장 오른쪽 아래까지 최단 거리 
    return graph[n-1][m-1]
print(bfs(0,0))