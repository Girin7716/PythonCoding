num = int(input())

for i in range(1,num+1):
    if i%3==0:
        print('X',end=" ")
    else:
        print(i,end=" ")