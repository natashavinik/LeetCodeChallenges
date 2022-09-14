class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        in_array = [[] for i in range(len(nums) + 1)]
        print(in_array)
        for x in nums:
            count[x] = count.get(x, 0) + 1
        for n, c in count.items():
            in_array[c].append(n)
        print(in_array)
        res = []
        for i in range(len(in_array) - 1, 0, -1):
            for n in in_array[i]:
                res.append(n)
                if len(res) == k:
                    return res
        # return res
            
        
                
            
            