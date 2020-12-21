# 모험가 길드, p311
import operator

N = int(input())
person = list(map(int,input().split()))

person.sort()

count = 0
group_cnt = 0
for i in person:
    count += 1
    if i <= count:
        group_cnt+=1
        count = 0

print(group_cnt)