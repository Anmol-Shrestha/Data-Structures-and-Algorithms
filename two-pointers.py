

"""
Two Pointers: The Trick is in How they move and Why they move
arrays are sorted: 

Category 1(Same direction): Fast and Slow pointers go to the same direction
Category 2(Opposite direction): 

Use case: 
1. Finding pairs
2. Symetric parts of a structure: Palindrome

Left pointer starts 0
Right pointer starts last index
Move the pointer based on some condition


Use for :
Palindrome
Reversals
merging sorted data
K sized comparisons

Ask Yourself: 
Can i do this my walkign the array once by both sides?
"""


"""
Palindrome
"""

input_string = input()
def is_palindrome(s):
    l, r = 0, len(s)-1
    while l<r:
        while l<r and not s[l].isalnum():
            l += 1
        while l<r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
        
    return True
        
    
    
    
is_palindrome(input_string)



"""
Fast and Slow Pointer
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        
    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        
    def print_node(self):
        temp = self.head
        while temp:
            print(temp.val)
            temp = temp.next
            
    def return_head(self):
        return self.head
    
        
        
            
        
        

linked_list = LinkedList(1)
linked_list.append(2)

print(linked_list)
linked_list.print_node()


linked_list.append(3)
linked_list.append(4)
linked_list.append(5)



def find_middle_node(ll):
    slow = fast = ll.return_head()
    
    
    while fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow.val


find_middle_node(linked_list)

    

