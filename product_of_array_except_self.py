class Solution:
    def product_except_self(self, nums: list[int]) -> list[int]:
        """
        Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

        The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

        You must write an algorithm that runs in O(n) time and without using the division operation.
        """
        

        answer: list[int] = []
        prefix_product = _prefix_product(nums)
        postfix_product = _postfix_product(nums)

        for i in range(len(nums)):
            answer.append(prefix_product[i] * postfix_product[i])
        return answer
    
def _prefix_product(nums: list[int]) -> list[int]:
    prefix_product: list[int] = [1]
    for i in range(len(nums) - 1):
        prefix_product.append(prefix_product[i] * nums[i])
    return prefix_product

def _postfix_product(nums: list[int]) -> list[int]:
    postfix_product: list[int] = [1]
    for i in range(len(nums) - 1, 0, -1):
        postfix_product.append(postfix_product[-1] * nums[i])
    postfix_product.reverse()
    return postfix_product
