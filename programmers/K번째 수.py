from numpy import sort
def solution(array, commands):
    answer = []
    #내풀이
    # for i in range(0,len(commands)):
    #     start=commands[i][0]-1
    #     end=commands[i][1]
    #     position=commands[i][2]-1
    #     num=array[start:end]
    #     num.sort()
    #     answer.append(num[position])

    # 다른 사람 풀이
    for command in commands:
        i, j, k = command
        answer.append((sorted(array[i - 1:j]))[k - 1])

        #return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands)) #list,map,lambda로 한줄로 표현 가능

    return answer
print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))