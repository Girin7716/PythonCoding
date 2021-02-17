## 모르겠음.

import math

print("start")

for _ in range(int(input())):
    a = -1
    d = 1
    n = int(input())
    while (2*n-d*d-d)/(2*(d+1)) > 0:
        if (2*n-d*d-d)%(2*(d+1)) == 0:
            a = (2*n-d*d-d)/(2*(d+1))
            b = a + d
            break
        d += 1

    if a == -1:
        print("IMPOSSIBLE")
    else:
        print("{} = {}".format(n,math.trunc(a)),end='')
        a+=1
        while a<=b:
            print(" + {}".format(math.trunc(a)),end='')
            a+=1
        print()

