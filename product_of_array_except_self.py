class Solution:
    def product_except_self(self, nums: list[int]) -> list[int]:
        """
        Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

        The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

        You must write an algorithm that runs in O(n) time and without using the division operation.
        """
        
        answer: list[int] = []
        for i in range(len(nums)):
            product: int = 1
            for j in range(len(nums)):
                if i != j:
                    product *= nums[j]
            answer.append(product)
        return answer
    
