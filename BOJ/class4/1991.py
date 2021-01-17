# 트리 순회
import sys
input = sys.stdin.readline

N = int(input())
graph = {}
for i in range(N):
    a,b,c = input().split()
    graph[a] = graph.get(a,[]) + [b]
    graph[a] = graph.get(a, []) + [c]
print(graph)
def preorder(node):
    if node == '.':
        return
    left = graph[node][0]
    right = graph[node][1]
    print(node,end = '')
    preorder(left)
    preorder(right)

def inorder(node):
    if node == '.':
        return
    left = graph[node][0]
    right = graph[node][1]
    inorder(left)
    print(node, end='')
    inorder(right)
def postorder(node):
    if node == '.':
        return
    left = graph[node][0]
    right = graph[node][1]
    postorder(left)
    postorder(right)
    print(node, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')

# 7
# A B C
# B D .
# C E F
# E . .
# F . G
# D . .
# G . .