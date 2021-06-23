def solution(answers):
    answer = []
    score = [0, 0, 0]
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i, num in enumerate(answers):
        ######print(i%len(a))   a,b,c배열의 크기가 다르기때문에 길이 나머지로 값을 나타내고 계산량 줄임
        if num == a[i%len(a)]:
            score[0] += 1
        if num == b[i%len(b)]:
            score[1] += 1
        if num == c[i%len(c)]:
            score[2] += 1
    for j, val in enumerate(score):
        if val == max(score):
            answer.append(j + 1)
    return answer


##########################최고 간결
    # p = [[1, 2, 3, 4, 5],
    #          [2, 1, 2, 3, 2, 4, 2, 5],
    #          [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    #     s = [0] * len(p)
    #
    #     for q, a in enumerate(answers):
    #         for i, v in enumerate(p):
    #             if a == v[q % len(v)]:
    #                 s[i] += 1
    #     return [i + 1 for i, v in enumerate(s) if v == max(s)]
print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))