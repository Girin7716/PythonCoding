# 커리큘럼
# 난이도3/3, 풀이 시간 50분, 시간 제한 2초, 메모리 제한 128MB
# 책에서 푼 방법
from collections import deque
import copy

v = int(input())
indegree = [0] * (v+1)
graph = [[] for i in range(v+1)]
time = [0] * (v+1)

for i in range(1,v+1):
    data = list(map(int,input().split()))
    time[i] = data[0]
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)

def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1,v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now]+time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in range(1,v+1):
        print(result[i])

topology_sort()

# # 내가 푼 방법(못품)
# from collections import deque
#
# # 노드의 개수와 간선의 개수를 입력받기
# v = int(input())
# # 모든 노드에 대한 진입차수는 0으로 초기화
# indegree = [0] * (v+1)
# # 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
# graph = [[] for i in range(v+1)]
#
# # 방향 그래프의 모든 간선 정보를 입력받기
# for i in range(v):
#     time = map(int(input().split()))
#     pre = map(int(input().split()))
#     while pre != -1:
#         graph[i].append(pre)
#         indegree[pre] += 1
#
#
# # 위상 정렬 함수
# def topology_sort():
#     result = [] # 알고리즘 수행 결과를 담을 리스트
#     q = deque() # 큐 기능을 위한 deque 라이브러리 사용
#
#     # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
#     for i in range(1,v+1):
#         if indegree[i] == 0:
#             q.append(i)
#
#     # 큐가 빌 때까지 반복
#     while q:
#         # 큐에서 원소 꺼내기
#         now = q.popleft()
#         result.append(now)
#         # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
#         for i in graph[now]:
#             indegree[i] -= 1
#             # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
#             if indegree[i] == 0:
#                 q.append(i)
#
#     # 위상 정렬을 수행한 결과 출력
#     for i in result:
#         print(i, end=' ')
#
# topology_sort()



# case1
# 5
# 10 -1
# 10 1 -1
# 4 1 -1
# 4 3 1 -1
# 3 3 -1

# 출력 예시
# 10
# 20
# 14
# 18
# 17