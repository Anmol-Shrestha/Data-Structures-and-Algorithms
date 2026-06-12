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
    

listlist = [4, 'h1', [5,4,3], 'yo', {'squirrel':'cute', 'Penguin':'Yummy'}]
print(listlist[4]['Penguin'])



y = list(range(5,16))
y
y[1:-1:2]



input_arr = [2, 3,4,5,6,7,8]

# reversing a list 

reversed = input_arr[::-1]
reversed


# Split Words
sentence = 'Words in a sentence are separated by spaces.'

sentence.split(' ')

newList = ''.join(sentence.split(' '))
newList

"""
SET : used for Tracker

"""
nums = [1,2,3,3,4,4,5,6,7]
set_num = set(nums) 
set_num

print(3 in set_num) # Faster than looping through the entire list







