def solution(numbers, hand):
    answer = ''
    lastL=10 #마지막 왼손 저장
    lastR=12 #마지막 오른손 저장
    for i in numbers:
        if i in [1,4,7]:
            answer += 'L'
            lastL = i #마지막 왼손 저장
        elif i in [3,6,9]:
            answer += 'R'
            lastR = i #마지막 오른손 저장
        else:
            if i==0:
                i=11
            absL=abs(i - lastL) #i와 마지막 왼손과 거리
            absR = abs(i - lastR) #i와 마지막 오른손과 거리
            #########divmod로 쉽게 표현
            if(sum(divmod(absL,3)))>sum(divmod(absR,3)): #오른쪽이 더 가깝다면
                answer += 'R'
                lastR=i #마지막 오른손 저장
            elif (sum(divmod(absL,3))) < sum(divmod(absR,3)): #왼쪽이 더 가깝다면
                answer += 'L'
                lastL = i #마지막 왼손 저장
            else: #거리가 같다면
                if (hand == "right"):
                    answer += 'R'
                    lastR = i #마지막 왼손 저장
                elif (hand == "left"):
                    answer += 'L'
                    lastL = i #마지막 왼손 저장
            # if (abs(numbers[i] - num1) / 3 + abs(numbers[i] - num1) % 3) > (
            #         abs(numbers[i] - num2) / 3 + abs(numbers[i] - num2) % 3): #########divmod로 쉽게 표현
            #     answer += 'L'
            # elif (abs(numbers[i]-num1) / 3+abs(numbers[i]-num1) % 3) < (abs(numbers[i]-num2) / 3+abs(numbers[i]-num2) % 3):
            #     answer += 'R'


    return answer
print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))