#최소힙 사용
#heapq.heapify(원래 리스트)->힙으로 전환
#heapq.heappush(리스트,item)->item삽입
#heapq.heappop(리스트)->최소원소 pop
import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)#scoville->heap으로 변환
    while scoville[0] <K:
        if len(scoville)>1:
            answer += 1
            heapq.heappush(scoville, heapq.heappop(scoville)+heapq.heappop(scoville)*2)
        else: #한개 남았을때
            return -1
    return answer

print(solution([1, 2, 3, 9, 10, 12],7))