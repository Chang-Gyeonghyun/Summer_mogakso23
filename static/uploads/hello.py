class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        stack = []
        result = []
        def dfs():
            if stack not in result:
                result.append(stack[:])
            for i in nums:
                if not stack or i >= stack[-1]:
                    stack.append(i)
                    dfs()
                    stack.pop()
        dfs()
        return result