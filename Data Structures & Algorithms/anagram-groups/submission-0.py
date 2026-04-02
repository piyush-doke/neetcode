class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        memory = dict()
        
        for i, s in enumerate(strs):  
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord('a')] += 1
            freq = tuple(freq)

            if memory.get(freq):
                memory[freq].append(s)
            else:
                memory[freq] = [s]

        return list(memory.values())
