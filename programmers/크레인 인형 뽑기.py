def solution(board, moves):
    answer = 0
    doll=[]
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0: #빈칸이 아니면
                doll.append(board[j][i-1])
                board[j][i-1]=0 ###빈칸으로 바꿔줌
                if len(doll) > 1:
                    if doll[-1] == doll[-2]:
                        doll.pop(-1)
                        doll.pop(-1)
                        answer += 2
                break
    return answer
print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))
