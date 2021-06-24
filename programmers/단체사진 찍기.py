####################################풀지못함
from itertools import permutations
def solution(n,data):
    answer=0
    people=['A','C','F','J','M','N','R','T']
    pairs = list(map(list, permutations(people, 8)))
    for i in pairs: #전체 경우의 쌍
        for j in data:
            first, second, case, num=j[0],j[2],j[3],int(j[4])
            n1 = i.index(first)
            n2 = i.index(second)
            if case == '=': ########전체 경우의 수- 아닌 경우의 수
                if int(abs(n1 - n2)) - 1 != num:
                    answer += 1
                    break ####다음 pair케이스로 넘어감
            elif case == '<':
                if int(abs(n1 - n2)) - 1 >= num:
                    answer += 1
                    break
            elif case == '>':
                if int(abs(n1 - n2)) - 1 <= num:
                    answer += 1
                    break
    return len(pairs)-answer
print(solution(2,["N~F=0", "R~T>2"]))