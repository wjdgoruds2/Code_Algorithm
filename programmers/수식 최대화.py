import re
from itertools import permutations
def solution(expression):
    answer=0
    per = list(permutations(list(set(re.sub("\d", "", expression))), len(list(set(re.sub("\d", "", expression))))))
    expression = re.split('([^0-9])', expression)
    max_sum = 0
    for ops in per:
        expression_copy = expression[:] ##########복사하는 이유: 연산자 조합 반복문이 돌아오면 다시 원래 리스트로 계산해야함((- * +)->(- + *).........)
        for op in ops:
            while op in expression_copy:
                idx=expression_copy.index(op)
                result=str(eval(expression_copy[idx-1]+expression_copy[idx]+expression_copy[idx+1]))
                expression_copy[idx - 1]=result
                expression_copy=expression_copy[:idx]+expression_copy[idx+2:]
        max_sum = max(max_sum, abs((int(expression_copy[-1])))) #########마지막엔 결국에 더한 값만 남음
    return max_sum
print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))