class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i,n in enumerate(nums):
            diff = target-n #check for the diff...
            if diff in prevMap:    #if diff is present, prevMap & curent index is returned          
                return [prevMap[diff],i]    
    #if not found,store current num nd index
            prevMap[n]=i

        