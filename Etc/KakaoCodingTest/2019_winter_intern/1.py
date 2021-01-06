def solution(board, moves):
    answer = 0
    stack = []

    for i in range(len(moves)):
        for j in range(len(board)):
            if board[j][moves[i]-1] != 0:
                stack.append(board[j][moves[i] - 1])
                board[j][moves[i] - 1]=0
                if len(stack)>=2 and stack[-1] == stack[-2]:
                    stack.pop()
                    stack.pop()
                    answer+=2
                break
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board,moves))