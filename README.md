
# 🚀 The 3-Phase DSA Blueprint
> Optimized for Engineering Assessments & Data Automation Tasks

### 📋 Phase 1: Input Analysis (Done with Interviewer)
Understanding the constraints changes how we approach the problem just like requirements gathering in real-world software project is the important phase in whole SDLC.

Phase 2 Heavily depends on how well we understand the problem.

*Understand the Input or ask for constraints*
Benefit? Interview will know you think about the system as a whole when designing a solution
* 📦 **Common Questions related to Integer:** 
  1. Are all the integers positive?, 
  2. Are there any duplicates numbers in the array?
  3. Will there always be a solution? because receiving an empty list, or insufficient items might not produce a solution
  4. What do we return if there is no solution?
  5. Can there be multiple pairs that add up to a value?


* 📦 **Write out some Test Cases:** 

TC1:   
```
array: [1,3]       target : 4   output: [0,1]
array: []          target : 4   output: 
array: [1]         target : 4   
array: [4,6,9,1,3] target : 4
```


  
---

### ⚙️ Phase 2: Processing Logic
*The Algorithmic Engine*

#### 🛑 1. Guard Clauses
* Instantly return base cases (e.g., `if not data: return 0`) to prevent runtime errors and system crashes.

#### 🎯 2. Strategy Selection Matrix
* **IF:** Processing contiguous blocks, sequential chunks, or substrings...
  * 🎯 *Strategy:* **Sliding Window** (Focuses on elements *inside* the bounds).
* **IF:** Working with sorted arrays, finding pairs, or analyzing extreme edges...
  * 🎯 *Strategy:* **Two-Pointer** (Focuses on elements *at* the bounds).
* **IF:** Tracking elements waiting for a trigger, next greater item, or height traps...
  * 🎯 *Strategy:* **Monotonic Stack** (Focuses on elements *history* until a wall hits).

#### 🗄️ 3. Initialization
* 🧠 **State Tracker:** Live history tracking (e.g., Hash Set, Dictionary, running total).
* 🏆 **Global Record Keeper:** A scalar variable storing the winning solution metric found so far.

#### 🔄 4. Traversal Engine & Triggers
* `pure for` ➔ Index-driven math (Fixed-size windows, direct slicing).
* `pure while` ➔ Boundaries closing in on each other (Opposite Two-Pointers).
* `while` inside `for` ➔ Steady expansion with conditional, rapid cleanups (Variable Window / Stack).

---

### 📦 Phase 3: Output Delivery
*Format and Ship the Result*
* 🔢 **Scalar Returns:** Return global max, min, or total counts directly.
* 🔪 **Slice Returns:** Use final saved pointer coordinates for an inclusive slice: `data[left : right + 1]`.
* ⚖️ **Existential Check:** Return early `True`/`False` states during triggers, with a safe fallback value.




# Before you start
Almost every interview question have three main components



## C1.  Variables to change depending on the Rules and Condition
SET is a data type that to track if something exists.

### Use cases of Set: 
1. Checking for duplicates
2. Checking for existence
3. Is the value in a current group
4. Sliding Window

## C2 Loops
1. for i in range(n)
2. for val in arr
3. while start < end

## C3 Rules and Conditions
4. if, else, elif
5. break, continue>


## Big O Notation
1. Binary Search : O(log n)
2. Loops/Traversing List: O(n)
3. Sorting  : O(n log n)
4. Nested Loops : O(n^2) # mainly brute force, not a viable solution for interview problem

### Optimization Trigger
if input is 10^4, we can use algorithm that is O(n^2)
If input size is 10^5, we would need to use algorithm that is O(n log n) or better



# Hash Maps
When brute force is too slow, we use Hash Map.
It's structured as key and value.
The valid key of a Hash Map cannot be changed.
So data type like list, dictionaries cannot be used as Keys of a Hashmap because they are mutable.
but data types like string, numbers, typles can be used.
They are Hashables.

### Without HashMap
Hash Map allows you to remember the answers as you go.
Imagine you had to do a complex calculation, you would want to store that isntead of doing it again.
HashMap allows you to do that when you are solving a problem.
Gives you a notebook that you can quickly check for answers.


No HashMap = O(n)
Hash Map = O(1)

```
my_map = {}

for item in items:
  if item not in my_map:
    my_map[item] = 1
  else:
    my_map[item] += 1

```
