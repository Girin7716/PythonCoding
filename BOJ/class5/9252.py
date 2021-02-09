# LCS2
data1 = ['0'] + list(input())
data2 = ['0'] + list(input())

d1_length = len(data1)
d2_length = len(data2)

dp = [[0 for _ in range(d1_length)] for _ in range(d2_length)]


for i in range(1,d2_length):
    for j in range(1,d1_length):
        if data2[i] != data1[j]:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        else:
            dp[i][j] = dp[i-1][j-1]+1

# for i in range(len(dp)):
#     for j in range(len(dp[i])):
#         print(dp[i][j],end= ' ')
#     print()

result = dp[-1][-1]
print(result)

rem = []
i,j = d2_length-1,d1_length-1
while i >=0 and j>=0:
    if dp[i][j] > dp[i][j-1] and dp[i][j] > dp[i-1][j]:
        rem.append(data1[j])
        i-=1
        j-=1
    elif dp[i][j-1] > dp[i-1][j]:
        j-=1
    else:
        i-=1
print(''.join(rem[::-1]))




# CAPCAK
# ACAYKP

# ACAYKP
# CAPCAK