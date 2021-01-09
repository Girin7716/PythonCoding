# 오큰수
import heapq
import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int,input().split()))

stack = []
result = []
index = 0
top = -1
while True:
    if index == N:
        break
    if len(stack)== 0:
        stack.append(index)
        top+=1
        index+=1
        continue
    if data[index] <= data[stack[top]]:
        stack.append(index)
        top+=1
        index+=1
    else:
        while stack:
            x = stack.pop()
            top-=1
            if data[x] >= data[index]:
                stack.append(x)
                top += 1
                break
            heapq.heappush(result,(x,data[index]))
            #result.append(data[index])

while stack:
    heapq.heappush(result,(stack.pop(),-1))

for i in range(N-1):
    rem = heapq.heappop(result)
    print(rem[1],end=' ')
rem = heapq.heappop(result)
print(rem[1])
