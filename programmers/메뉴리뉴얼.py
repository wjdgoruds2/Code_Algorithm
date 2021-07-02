from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    per=[]
    for num in course:
        per = []
        for order in orders:
            for li in combinations(order,num):
                res = ''.join(sorted(li))#############조합을 만들면서 정렬
                per.append(res)
        sorted_candidates = Counter(per).most_common() ########가장 높은 순으로
        print(sorted_candidates)
        answer += [menu for menu, cnt in sorted_candidates if cnt > 1 and cnt == sorted_candidates[0][1]]
    return sorted(answer)
print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))
print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))