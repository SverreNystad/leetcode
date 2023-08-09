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
        if len(flowerbed) == 1:
            if flowerbed[0] == Bed.EMPTY.value:
                flowerbed[0] = Bed.PLANTED.value
                planted += 1

        for i, bed in enumerate(flowerbed):
            if bed == Bed.PLANTED.value:
                continue

            # Check edges
            if i == 0:
                # Check if next bed is empty
                if flowerbed[i + 1] == Bed.EMPTY.value:
                    flowerbed[i] = Bed.PLANTED.value
                    planted += 1
                continue
            if i == len(flowerbed) - 1:
                # Check if previous bed is empty
                if flowerbed[i - 1] == Bed.EMPTY.value:
                    flowerbed[i] = Bed.PLANTED.value
                    planted += 1
                continue

            # Check if previous bed is empty
            if i < len(flowerbed) - 1:
                if flowerbed[i - 1] == Bed.EMPTY.value and flowerbed[i + 1] == Bed.EMPTY.value:
                    flowerbed[i] = Bed.PLANTED.value
                    planted += 1

        return planted >= n


class Bed(Enum):
    EMPTY = 0
    PLANTED = 1
