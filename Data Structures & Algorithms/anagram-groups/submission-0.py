class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams=[]
        seen = [False] * len(strs)
        for i in range(len(strs)):
            if seen[i]:
                continue
            res = [strs[i]]
            seen[i] = True
            for j in range(i+1,len(strs)):
                if not seen[j]:
                    if sorted(strs[i])==sorted(strs[j]):
                        res.append(strs[j])
                        seen[j] = True
            
            anagrams.append(res)

        return anagrams
                