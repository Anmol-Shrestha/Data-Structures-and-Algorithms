"""
Move Zeroes to the end.
The input: [0,1,0,3,12]
The expected output array : [1,3,12,0,0]


Phase 1: Input Analysis

Does the input always have zeroes?
Is the order of non-zero number supposed to be preserved or sorted in ascending or descending order?
What are the constraints?
1. inplace reorganization


Strategy: Since we are supposed to re-organize inplace, we need to use two-pointer same direction partiioning pattern

"""

nums = [0, 1, 12, 3,0 ]

# we have two pointers starting at 0 and alnother pointer looping from 0
# Guard Clauses : Empty Array 

slow = 0

for fast in range(len(nums)):
    if nums[fast] != 0:
        nums[slow],nums[fast]= nums[fast],nums[slow]
        slow += 1

print(nums)
    







