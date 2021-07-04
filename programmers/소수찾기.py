from itertools import permutations
def solution(numbers):
    arr = list(numbers)
    num_arr=[]
    count=0
    for i in range(1,len(arr)+1):
        num_arr+=list(permutations(arr,i))
    for j in range(len(num_arr)):
        num_arr[j]=int(''.join(num_arr[j]))
    print(set(num_arr))
    for k in set(num_arr):
        if is_prime(k) is not False:
            count+=1
    return count
def is_prime(num):
    if num == 1 or num ==0:
        return False
    if num==2 or num ==3:
        return True
    for i in range(2,num//2+1):
        if num % i ==0:
            return False
print(solution("17"))
print(solution("011"))
print(solution("127"))