from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        # Make a dict for each unique value increment for each key value pair and find max
        numbers = {}

        for number in arr:
            if number in numbers.keys():
                amount = numbers.get(number)
                numbers[number] = amount + 1
            else:
                numbers[number] = 1

        return len(numbers.values()) == len(set(numbers.values()))
