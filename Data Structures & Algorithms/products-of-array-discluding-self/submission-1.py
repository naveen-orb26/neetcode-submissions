class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        pval=sval = 1
        for num in nums:
            pval*=num
            prefix.append(pval)
        for num in nums[::-1]:
            sval*=num
            suffix.append((sval))
        ans = []
        for i in range(len(nums)):
            if i==0:
                target=suffix[len(nums)-2]
            elif i ==len(nums)-1:
                target=prefix[len(nums)-2]
            else:
                target = prefix[i-1]*suffix[len(nums)-i-2]
            ans.append(target)
        return ans