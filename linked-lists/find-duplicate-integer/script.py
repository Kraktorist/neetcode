#!/usr/bin/env python
from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        first, second = 0, 0
        while True:
            first = nums[first]
            second = nums[nums[second]]
            if first == second:
                break

        second = 0
        while True:
            first = nums[first]
            second = nums[second]
            if first == second:
                return second

