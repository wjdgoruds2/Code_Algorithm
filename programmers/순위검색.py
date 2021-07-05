import re
def solution(info, query):
    answer = []
    arr=[]
    new_q=[]
    length=len(info)
    for i in range(length):
        arr.append(list(info[i].split(' ')))
    for j in range(length):
        new_q.append(list(re.split(' and | ',query[j])))
    for n in range(length):
        count = 0
        for j in range(length):
            if new_q[n][:-1]== arr[j][:-1] and int(new_q[n][-1])<=int(arr[j][-1]):
                count+=1
            elif '-' in new_q[n]:
                sub= list(set(new_q[n][:-1]) - set(arr[j][:-1] ))
                if (set(sub)=={'-'})== True and int(new_q[n][-1])<=int(arr[j][-1]):
                    count+=1
        answer.append(count)
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