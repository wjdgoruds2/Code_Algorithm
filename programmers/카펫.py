def solution(brown, yellow):
    answer = []
    width=0
    height=0
    total=brown+yellow
    for i in range(1,total//2):
        width=i
        if total%width==0:
            height=total//i
            if (width-2)*(height-2)==yellow:
                if width>=height:
                    return[width,height]
print(solution(10,2))
print(solution(8,1))
print(solution(24,24))