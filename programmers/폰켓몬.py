def solution(nums):
    answer = 0
    length=len(nums)//2 #int(len(nums)/2)
    nums=list(set(nums))
    if length<len(nums):
        answer=length
    else:
        answer = len(nums)
    return answer
 #어차피 원래 배열 길이 vs 중복 제거 배열 길이
    #return min(len(nums)//2, len(set(nums)))
print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))