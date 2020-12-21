# 문자열 뒤집기 / p313

S = input()

dict = {'0':0,'1':0}

for i in range(1,len(S)-1):
    if S[i] != S[i-1]:
        dict[S[i-1]]+=1
    if i == len(S)-1:
        dict[S[i]]+=1

print(min(dict.values()))

# # 책에서 풀이법
# data = input()
# count0 = 0
# count1 = 0
# if data[0] == '1':
#     count0+=1
# else:
#     count1 += 1
#
# for i in range(len(data)-1):
#     if data[i] != data[i+1]:
#         if data[i+1] == '1':
#             count0 += 1
#         else:
#             count1 +=1
# print(min(count0,count1))