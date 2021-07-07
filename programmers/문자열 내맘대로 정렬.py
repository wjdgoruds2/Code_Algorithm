def solution(strings, n):
    # answer = []
    # sor=[]
    # strings.sort()
    # for i in strings:
    #     sor+=i[n]
    # sor.sort()
    # for i in sor:
    #     for j in strings:
    #         print(i,j)
    #         if i in j[n]:
    #             if j not in answer:
    #                 answer.append(j)
    # return answer
    return sorted(strings,key=(lambda s:[s[n],s]))#n번째 문자를 우선적으로 처리하고 그 다음 나머지를 처리

print(solution(["sun", "bed", "car"],1))
print(solution(["abce", "abcd", "cdx"],2))
