# 트리의 순회
import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n = int(input())
inorder = list(map(int,input().split()))
postorder = list(map(int,input().split()))

pos = [0] *(n+1)
for i in range(n):
    pos[inorder[i]] = i

def divide(in_start,in_end,post_start,post_end):
    if (in_start > in_end) or (post_start > post_end):
        return

    root = postorder[post_end]
    print(root, end=' ')

    # left tree
    divide(in_start,pos[root]-1,post_start,post_start+pos[root]-in_start-1)
    # right tree
    divide(pos[root]+1,in_end,post_start+pos[root]-in_start,post_end-1)


divide(0,n-1,0,n-1)

# 3
# 1 2 3
# 1 3 2

# 7
# 4 2 5 1 6 3 7
# 4 5 2 6 7 3 1

# https://whereisend.tistory.com/112