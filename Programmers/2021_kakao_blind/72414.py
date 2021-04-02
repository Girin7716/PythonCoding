# 광고 삽입

def makeSecond(time):
    time = time.split(':')
    second = int(time[0])*3600+int(time[1])*60+int(time[2])
    return second

def makeTime(second):
    h=second//3600
    m=(second-(h*3600))//60
    s=(second-(h*3600)-(m*60))
    return str(h).zfill(2)+":"+str(m).zfill(2)+":"+str(s).zfill(2)

def solution(play_time, adv_time, logs):
    answer =''
    play_time = makeSecond(play_time)
    adv_time = makeSecond(adv_time)

    # 시청자 수 메모
    memo = [0 for _ in range(play_time+1)]
    for log in logs:
        start, end = log.split('-')
        start = makeSecond(start)
        end = makeSecond(end)

        memo[start] += 1
        memo[end] -= 1

    # 누적 시청자 수 메모
    # 1) 현재 시청자 수
    for i in range(1,play_time+1):
        memo[i] = memo[i] + memo[i-1]
    # 2) 누적 시청자 수
    for i in range(1,play_time+1):
        memo[i] = memo[i] + memo[i-1]

    max_play = memo[adv_time-1]
    start = 0
    for i in range(adv_time,play_time):
        play = memo[i] - memo[i-adv_time]

        if play > max_play:
            max_play = play
            start = i - adv_time+1
    answer=makeTime(start)

    return answer

# def solution(play_time, adv_time, logs):
#     answer = ''
#     play_time = makeSecond(play_time)
#
#     adv_time = makeSecond(adv_time)
#
#     logs_second = []
#     logs_rem = []
#     for log in logs:
#         a,b = log.split('-')
#         log = str(makeSecond(a)) + '-' + str(makeSecond(b))
#         logs_second.append(log)
#         heapq.heappush(logs_rem,makeSecond(a))
#         heapq.heappush(logs_rem, makeSecond(b))
#         # logs_rem.append(makeSecond(a))
#         # logs_rem.append(makeSecond(b))
#     # logs_rem.append(0)
#     heapq.heappush(logs_rem,0)
#     # logs_rem.sort()
#
#     sum_log = [0] * (100*3600)
#     for log in logs_second:
#         start,end = log.split('-')
#         for i in range(int(start),int(end)):
#             sum_log[i] += 1
#
#     max_value = 0
#     max_second = 0
#     # for start in logs_rem:
#     while logs_rem:
#         start = heapq.heappop(logs_rem)
#         end = start + adv_time
#         if end > play_time:
#             break
#         sum_value = sum(sum_log[start:end])
#         if max_value < sum_value:
#             max_value = sum_value
#             max_second = start
#
#     answer = makeTime(max_second)
#
#     return answer

#"01:30:59"
print(solution("02:03:55","00:14:15",["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
#"01:00:00"
print(solution("99:59:59","25:00:00",["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
#"00:00:00"
print(solution("50:00:00","50:00:00",["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))
