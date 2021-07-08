##############################함수를 씁시다.
def to_list(arr):
    xy=[]
    belen=[]
    new_arr=[new for new in arr]
    for i in range(5):
        for j in range(5):
            if new_arr[i][j] == 'P':
                xy.append([i, j])
    for f in range(len(xy)):
        for s in range(f+1,len(xy)):
            belen.append([manhatten(xy[f],xy[s]),xy[f],xy[s]])
    for ver in belen:
        print(ver)
        if ver[0]==0:
            continue
        elif ver[0]==1:
            return 0
        elif ver[0]==2:
            print("case",ver[1],ver[2])
            mid_x=(ver[1][0]+ver[2][0])//2
            mid_y = (ver[1][1] + ver[2][1]) // 2
            if new_arr[ver[1][0]][ver[2][1]]=='O' or new_arr[ver[2][0]][ver[1][1]]=='O': #######PO OP 나 PO XP처럼 책상이 하나라도 있을 경우
                return 0
            elif new_arr[ver[1][0]][mid_y]=='O' or new_arr[mid_x][ver[1][1]]=='O':#######가로 세로 'POP'경우
                return 0
    return 1
def manhatten(first,second):
    return (abs(first[0] - second[0]) + abs(first[1] - second[1]))
def solution(places):
    answer = []
    for arr in places:
        answer.append(to_list(arr))
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
                ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
                ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
