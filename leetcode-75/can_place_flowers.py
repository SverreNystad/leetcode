from enum import Enum


class Solution:
    def can_place_flowers(self, flowerbed: list[int], n: int) -> bool:
        """
        You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

        Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
        """

        # Edge case: empty flowerbed
        if len(flowerbed) == 0:
            return False

        planted: int = 0
        # Edge case: flowerbed of length 1
        i = 0
        while i < len(flowerbed):
            # Escape early if all needed flowers have been planted
            if planted == n:
                return True
            # Skip to next empty plot
            if flowerbed[i] == Bed.PLANTED.value:
                i += 2
            # Skip to next empty plot if the next plot is planted
            elif i < len(flowerbed) - 1 and flowerbed[i + 1] == Bed.PLANTED.value:
                i += 3
            # Plant flower
            else:
                flowerbed[i] = Bed.PLANTED.value
                planted += 1
        return False


class Bed(Enum):
    EMPTY = 0
    PLANTED = 1
