# 반복은 해야겠는데, 몇번 반복해야할지 모르겠을 때

day = 0
a = 10

while True:
    if a >= 100:
        break
    a *= 1.1
    day += 1
print(day)
