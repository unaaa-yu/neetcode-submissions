class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            if i == 0:
                ans.append(1)
            else:
                ans.append(ans[i-1] * nums[i-1])
        
        postfix = 1
        for i in range(-1, -len(nums) - 1, -1):
            if i != -1:
                postfix *= nums[i+1] 
            ans[i] *= postfix
        
        return ans

        