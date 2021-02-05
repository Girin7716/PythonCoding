from itertools import combinations as cb
import sys
input=sys.stdin.readline

if __name__ == "__main__":
    cnt = 0
    n, s = map(int, input().split())
    arr = [*map(int, input().split())]
    for i in range(1, n + 1):
        for combination in cb(arr,i):
            if sum(combination) == s:
                #print(combination)
                cnt += 1
    print(cnt)
