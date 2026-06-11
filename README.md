# 🚀 The 3-Phase DSA Blueprint
> Optimized for Engineering Assessments & Data Automation Tasks

---

### 📋 Phase 1: Input Analysis
*Deconstruct the Data Payload*
* 📦 **Shape Check:** Is it a List, String, Tuple, Matrix, or Stream?
* 📏 **Sizing:** Can it be empty? Does it have only 1 element? What are the bounds?
* 🔀 **Order:** Is the input pre-sorted, unsorted, or reverse-ordered?
* 🆔 **Duplicates:** Are duplicate values present? Do we need unique items?

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
