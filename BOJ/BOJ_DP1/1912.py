# 연속합
import sys
import copy
input = sys.stdin.readline

N = int(input())
data = list(map(int,input().split()))
dp = copy.deepcopy(data)

for i in range(1,len(data)):
    dp[i] = max(dp[i-1]+data[i],data[i])

print(max(dp))