# 트리의 지름
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
for i in range(n-1):
    a,b,w = map(int,input().split())
    graph[a].append((b,w))
    graph[b].append((a,w))

def dfs(start):
    stack = []
    visited = [False] * (n+1)
    stack.append((start,0)) # node, value
    max_value = 0
    while stack:
        v,dist = stack.pop()
        visited[v] = True
        for next in graph[v]:
            if visited[next[0]] == False:
                if max_value < next[1]+dist:
                    max_value = next[1]+dist
                stack.append((next[0],next[1]+dist))

    return max_value

max_value = 0
for i in range(1,n):
    visited = [False] * (n + 1)
    result = dfs(i)
    if max_value < result:
        max_value = result

print(max_value)

# 12
# 1 2 3
# 1 3 2
# 2 4 5
# 3 5 11
# 3 6 9
# 4 7 1
# 4 8 7
# 5 9 15
# 5 10 4
# 6 11 6
# 6 12 10