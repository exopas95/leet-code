class Solution:
    def reverseWords(self, s: str) -> str:
        sList = s.split(' ')
        rList = []
        for word in sList:
            rList.append(word[::-1])
        
        answer = ' '.join(rList)
        return answer
            