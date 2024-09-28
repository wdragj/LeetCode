class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for str in strs:
            if "".join(sorted(str)) not in hashmap:
                hashmap["".join(sorted(str))] = [str]
            else:
                hashmap["".join(sorted(str))].append(str)
        
        return(list(hashmap.values()))
