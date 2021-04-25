# 단속카메라
def solution(routes):
    answer = 1

    routes.sort(key=lambda x:x[1])
    nowCamera = routes[0][1]
    for route in routes:
        if nowCamera < route[0]:
            nowCamera = route[1]
            answer += 1

    return answer

print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))
print(solution([[-20,15],[17,19]]))
print(solution([[-20,15],[15,30]]))