class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)

        for num in nums:
            hashmap[num] += 1
        
        sorted_dict = dict(sorted(hashmap.items(), key=lambda x: x[1], reverse=True))
        res = list(sorted_dict.keys())
        return(res[0:k])