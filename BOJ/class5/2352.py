# 반도체 설계
import sys
input = sys.stdin.readline

n = int(input())
lines = list(map(int,input().split()))

def binary_search(line,cnt):
    left = 0
    right = cnt

    index = 0
    while left<=right:
        mid = (left+right)//2
        if lis[mid] > line:
            right = mid - 1
            index = mid
        else:
            left = mid + 1
    lis[index] = line

cnt = 1
lis = [lines[0]]
for line in lines[1:]:
    if lis[-1] < line:
        lis.append(line)
        cnt+=1
    else:
        binary_search(line, cnt)

print(cnt)