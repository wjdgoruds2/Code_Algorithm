import collections
from typing import List
class Test:

    def groupAnagrams(self, strs: List[str])->List[List[str]]:
        anagrams=collections.defaultdict(list)

        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        return list(anagrams.values())
w1=Test()
print(w1.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))