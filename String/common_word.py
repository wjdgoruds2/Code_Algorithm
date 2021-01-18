#애너그램 (단어를 알파벳 순으로 정렬해서 같은 것끼리 list형성해서 출력)
import collections
from typing import List

class Test:

    def groupAnagrams(self, strs:List[str])->List[List[str]]:
        anagrams=collections.defaultdict(list)

        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        return list(anagrams.values())
w1=Test()
print(w1.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

#파이썬 정렬은 Timsort사용
#퀵소트가 가장 빠르다고 알려져있지만 병합 정렬이 일정하게 안정적인 성능을 보여 안정정렬이라는 점에서 병합 정렬이 많이 선호되는 편이다.
#주의:sorted 와 sort는 다른것으로 주의!
#sort()함수는 None을 리턴


a=['cde','cfc','abc']  #단어의 첫번째를 기준으로 정렬하고 같으면 마지막 문자를 비교해서 정렬
#방법1
# def fn(s):
#     return s[0],s[-1]
# print(sorted(a,key=fn))

#방법2
# b=sorted(a,key=lambda s:(s[0],s[-1]))
# print(b)
