class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.largest = k - 1
        # self.nums = nums.sort(reverse = True)
        self.nums = sorted(nums, reverse = True)

    def add(self, val: int) -> int:
        leng = len(self.nums)
        for i in range(len(self.nums)):
            if val >= self.nums[i]:
                self.nums.insert(i, val)
                break
        if leng == len(self.nums):
            self.nums.append(val)
        return self.nums[self.largest]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)