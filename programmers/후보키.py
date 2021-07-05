from itertools import combinations
def solution(relation):
    row = len(relation)
    col = len(relation[0])

    candidates = []
    final=[]
    #전체 조합
    for i in range(1, row + 1):
        candidates.extend(combinations(range(col), i))
    #유일성
    for keys in candidates:
        print(keys)
        tmp=[tuple([item[key] for key in keys]) for item in relation] #item [0]별 [1]별.... tuple에 저장
        print(tmp)
        if len(set(tmp)) == row:
            final.append(keys)
        answer=set(final[:])
    # 최소성
    for i in range(len(final)):
        for j in range(i+1,len(final)):
            if len(final[i])==len(set(final[i]).intersection(set(final[j]))): ########뒤에 있는 경우의 수들중 앞에 있는 경우의 수가 있으면 최소성 만족
                answer.discard(final[j])
    print(answer)
    return len(answer)
    



#     answer = 0
#     arr_row={}
#     com_list=[]
#     for num in range(0,len(relation[0])):
#         row = []
#         for arr in relation:
#             row.append(arr[num])
#         arr_row[num]=row
#         print(arr_row)
#     for i in range(2,len(arr_row)):
#         com_list.append(list(combinations(arr_row.values(),i)))
#     for j in range(len(com_list)):
#         print(j)
#         for z in com_list[j]:
#             print(list(combinations(z,2)))
#     print("sk",com_list)
# def is_correct(arr,count):
#     if count==1:
#         ver=set(arr)
#         if len(ver)==len(arr):
#             return True

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],
                ["300","tube","computer","3"],["400","con","computer","4"],
                ["500","muzi","music","3"],["600","apeach","music","2"]]))