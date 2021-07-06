import re
##############################정확성은 통과하는데 효율성은 통과하지 못한 코드##############################
# def solution(info, query):
#     answer = []
#     arr=[]
#     new_q=[]
#     length=len(info)
#     for i in range(length):
#         arr.append(list(info[i].split(' ')))
#     for j in range(length):
#         new_q.append(list(re.split(' and | ',query[j])))
#     for n in range(length):
#         count = 0
#         for j in range(length):
#             if new_q[n][:-1]== arr[j][:-1] and int(new_q[n][-1])<=int(arr[j][-1]):
#                 count+=1
#             elif '-' in new_q[n]:
#                 sub= list(set(new_q[n][:-1]) - set(arr[j][:-1] ))
#                 if (set(sub)=={'-'})== True and int(new_q[n][-1])<=int(arr[j][-1]):
#                     count+=1
#         answer.append(count)
#     return answer

##################################################방법1
# from itertools import combinations
# from bisect import bisect_left
# def make_arr(arr):
#     cases=[]
#     for i in range(5): ############네가지 파트의경우의 수(0~4까지의 조합)
#         for li in combinations([0, 1, 2, 3], i):
#             case=''
#             for idx in range(4):#배열 0~3까지
#                 if idx not in li:
#                     case+=arr[idx]
#                 else:
#                     case += '-' #######'----'은 모든 경우의 수
#             cases.append(case) ###########################16가지 경우의 수
#     return cases
#
# def solution(info, query):
#     answer=[]
#     all_people={}
#     for i in info:
#         sep_info=i.split()
#         cases=make_arr(i.split())
#         for case in cases:
#             if case not in all_people.keys():all_people[case]=[int(sep_info[4])] #########점수입력
#             else:all_people[case].append(int(sep_info[4])) #####동일 케이스에선 점수 뒤에 더함
#     for key in all_people.keys():
#         all_people[key].sort()   #######점수 배열
#
#     for q in query:
#         sep_q=q.split()
#         tar=sep_q[0]+sep_q[2]+sep_q[4]+sep_q[6]
#         if tar in all_people.keys():
#             answer.append(len(all_people[tar])- bisect_left(all_people[tar],int(sep_q[7])))
#             ######배열 이진 분할 알고리즘(left:배열된 왼쪽의 개수, right:배열된 오른쪽의 개수(크거나 같은거 개수))
#         else:
#             answer.append(0)
#     return answer


##################################################방법2
def solution(info, query):
    data = dict()
    for a in ['cpp', 'java', 'python', '-']:
        for b in ['backend', 'frontend', '-']:
            for c in ['junior', 'senior', '-']:
                for d in ['chicken', 'pizza', '-']:
                    data.setdefault((a, b, c, d), list())
    for i in info:
        i = i.split()
        for a in [i[0], '-']:
            for b in [i[1], '-']:
                for c in [i[2], '-']:
                    for d in [i[3], '-']:
                        data[(a, b, c, d)].append(int(i[4]))

    for k in data:
        data[k].sort()

    answer = list()
    for q in query:
        q = q.split()

        pool = data[(q[0], q[2], q[4], q[6])]
        find = int(q[7])
        l = 0
        r = len(pool)
        mid = 0
        while l < r:
            mid = (r+l)//2
            if pool[mid] >= find:
                r = mid
            else:
                l = mid+1
            # print(l, r, mid, answer)
        # answer.append((pool, find, mid))
        answer.append(len(pool)-l)

    return answer


print(solution(["java backend junior pizza 150",
                "python frontend senior chicken 210",
                "python frontend senior chicken 150",
                "cpp backend senior pizza 260",
                "java backend junior chicken 80",
                "python backend senior chicken 50"],

               ["java and backend and junior and pizza 100",
                "python and frontend and senior and chicken 200",
                "cpp and - and senior and pizza 250",
                "- and backend and senior and - 150",
                "- and - and - and chicken 100",
                "- and - and - and - 150"]))