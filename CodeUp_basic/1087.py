num = int(input())

sum = 1
for i in range(2,num+1):
    if sum >= num:
        break;
    sum+=i
print(sum)