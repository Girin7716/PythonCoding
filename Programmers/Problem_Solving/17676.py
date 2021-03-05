# 추석 트래픽
def solution(lines):
    answer = 0

    rem = []    #[start,end]
    for line in lines:
        end_time = 0
        sec = 3600
        a,b,c = line.split()
        for i in str(b).split(':'):
            end_time += float(i) * sec
            sec/=60
        strat_time = round(end_time - float(c[:-1]) + 0.001,3)
        rem.append([strat_time,end_time])

    def check(time):
        start = time
        end = round(time + 0.999,3)

        result = 0

        for r in rem:
            r_start, r_end = r
            if r_end < start or r_start > end:
                continue
            result+=1
        return result

    for r in rem:
        start,end = r
        answer = max(answer,check(start),check(end))

    return answer

print(solution([
"2016-09-15 01:00:04.001 2.0s",
"2016-09-15 01:00:07.000 2s"
]))

print(solution([
"2016-09-15 01:00:04.002 2.0s",
"2016-09-15 01:00:07.000 2s"
]))

print(solution([
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]))
