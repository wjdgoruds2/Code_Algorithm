def solution(a, b):
    answer = ''
    totaldate=0
    date=[31,29,31,30,31,30,31,31,30,31,30,31]
    # day=['SUN','MON','TUE','WED','THU','FRI','SAT']
    day = ['FRI', 'SAT','SUN', 'MON', 'TUE', 'WED', 'THU']
    return day[(sum(date[:a-1])+b-1)%7]
    # for i in range(a-1):
    #     totaldate+=date[i]
    # totaldate+=b
    # rest=totaldate%7
    # loc=day.index('FRI')+(rest-1)
    # if loc>len(day)-1:
    #     loc=loc-len(day)
    # return day[loc]
print(solution(5,24))