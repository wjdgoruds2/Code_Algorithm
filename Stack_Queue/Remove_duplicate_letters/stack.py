import collections
class Solution:

    def removeDuplicateLetters(self,s:str)->str:
        counter,seen,stack = collections.Counter(s),set(),[]
        for char in s:
            counter[char]-=1
            if char in seen:
                continue   #이미 전에 중복 되었던 문자 인식 후 , for문으로 돌아감
            while stack and char < stack[-1] and counter[stack[-1]]>0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)

        return ''.join(stack)

t=Solution()
print(t.removeDuplicateLetters("bcabcb"))
