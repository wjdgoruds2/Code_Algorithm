def solution(arr1, arr2):
    # answer=[]
    # for i in range(len(arr1)):
    #     temp_lst = []
    #     for j in range(len(arr2[0])):
    #         temp = 0
    #         for k in range(len(arr2)):
    #             temp += arr1[i][k] * arr2[k][j]
    #         temp_lst.append(temp)
    #     answer.append(temp_lst)
    # return answer

    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*arr2)] for A_row in arr1] #zip(*)->행과 열을 바꿔줌
print(solution([[1, 4], [3, 2], [4, 1]],[[3, 3], [3, 3]]))
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]],[[5, 4, 3], [2, 4, 1], [3, 1, 1]]))