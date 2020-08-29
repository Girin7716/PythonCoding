# 리스트든 스트링이든


a = 'kimkihyun'
b = [1, 2, 3, 4, 5]

print(a[2:6])  # index 2부터 (6-2)개 or index 2부터 6전까지
print(b[2:4])  # index 2부터 (4-2)개 or index 2부터 4전까지

s = slice(0, 5, 2)  # 시작인덱;스, ~전까지 인덱스, 스텝

print(a[s])
print(b[s])

# list,str,튜플,레인지... 모두 적용 가능
