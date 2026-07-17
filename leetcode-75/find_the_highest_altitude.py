class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        altitude = 0
        max_altitude = 0
        for step in gain:
            altitude += step
            if altitude > max_altitude:
                max_altitude = altitude
        return max_altitude
