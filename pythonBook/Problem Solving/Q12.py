# 기동과 보 설치 / p329 / 구현 문제 / (실패)
# 책에서 푼 방법
def possible(answer):
    # answer에 있는 모든 구조물이 정상적인지 판단
    for x,y,stuff in answer:
        if stuff == 0: # 설치된 것이 기둥
            # 기둥이 바닥위 or '보의 한쪽 끝 부분' or '다른 기둥 위' 라면 정상
            if y == 0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
                continue
            return False
        elif stuff == 1:    # 보인 경우
            # '한쪽 끝부분이 기둥 위' or '양쪽 끝부분이 다른 보와 동시에 연결'이면 정상
            if [x,y-1,0] in answer or [x+1, y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x,y,stuff,operate = frame
        if operate == 0:    # 삭제
            answer.remove([x,y,stuff])  # 일단 삭제
            if not possible(answer):    # 가능한가?
                answer.append([x,y,stuff])  # 가능한게 아니면 다시 설치
        if operate == 1:    # 설치
            answer.append([x,y,stuff])  # 일단 설치
            if not possible(answer):    # 가능한가?
                answer.remove([x,y,stuff])  # 가능한게 아님 == 제거
    return sorted(answer)

print(solution(5,[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1,],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0,],[1,1,1,0],[2,2,0,1]]))