"""
Example Problem: Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

nums = [2,1,11,15]
target = 9

def two_sum(nums, target):
    ## Guard Clauses
    if not nums:
        return 
    if len(nums)<2:
        return 
    
    # After Deciding on the Strategy : HashMap for lookups, One pointer For Loop
    ## Variable Initialization
    my_map = {}
    
    ## Traversal Mechanism
    for idx, num in enumerate(nums):
        ntf = target - num
        if ntf in my_map:
            return [my_map[ntf], idx]
        my_map[num] = idx
        
    
    return f"Two Sum Does Not Exist for target : {target}"
        
two_sum(nums, target)


# First we understand the question properly
# Second we choose the strategy: HashMap + One Pointer
# Third we initialize the variables and loop: Variable for HashMap, Loop for the pointer
# We create the traversal mechanism

    
    
