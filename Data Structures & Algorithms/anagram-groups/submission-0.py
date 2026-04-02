class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myMap = {}

        for word in strs:
            srtd = sorted(word)
            srtd = "".join(srtd)

            if srtd in myMap:
                myMap[srtd].append(word)
            else:
                myMap[srtd] = [word]
            
        return list(myMap.values())