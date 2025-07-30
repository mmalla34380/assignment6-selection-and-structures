# Assignment 6: Medians and Order Statistics & Elementary Data Structures

Overview
This repository contains implementations and analysis of selection algorithms and elementary data structures. The project is divided into two main parts:

Selection Algorithms: Implementation and comparison of randomized and deterministic algorithms for finding the k<sup>th</sup> smallest element
Elementary Data Structures: From-scratch implementation of arrays, stacks, queues, and linked lists



# Part 1: Selection Algorithms
Algorithms Implemented

Randomized Quickselect

Expected O(n) time complexity
Worst-case O(n²) time complexity
O(1) space complexity (in-place)


Deterministic Selection (Median of Medians)

Guaranteed O(n) worst-case time complexity
O(n) space complexity



How to Run
bash# Navigate to Part1 directory
cd Part1_Selection_Algorithms/

# Run individual algorithm tests
python randomized_selection.py
python deterministic_selection.py

# Run performance comparison
python performance_test.py
Sample Usage
pythonfrom randomized_selection import quickselect
from deterministic_selection import deterministic_select

# Find 3rd smallest element in array
arr = [64, 34, 25, 12, 22, 11, 90]
k = 3

result1 = quickselect(arr.copy(), k)
result2 = deterministic_select(arr.copy(), k)
print(f"3rd smallest element: {result1}")  # Should match result2
# Part 2: Elementary Data Structures
Data Structures Implemented

Array: Dynamic array with insert, delete, and access operations
Stack: LIFO (Last In, First Out) structure
Queue: FIFO (First In, First Out) structure
Linked List: Singly linked list with traversal capabilities

How to Run
bash# Navigate to Part2 directory
cd Part2_Data_Structures/

# Run individual data structure tests
python array.py
python stack.py
python queue.py
python linked_list.py

# Run comprehensive demonstration
python demo_data_structures.py
Sample Usage
python# Array operations
from array import DynamicArray
arr = DynamicArray()
arr.insert(0, 10)
arr.insert(1, 20)
print(arr.access(0))  # Output: 10

# Stack operations
from stack import Stack
stack = Stack()
stack.push(10)
stack.push(20)
print(stack.pop())  # Output: 20

# Queue operations
from queue import Queue
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
print(queue.dequeue())  # Output: 10

# Linked List operations
from linked_list import LinkedList
ll = LinkedList()
ll.insert_at_head(10)
ll.insert_at_head(20)
ll.display()  # Output: [20, 10]
Key Findings
Selection Algorithms

Randomized Quickselect performs better on average due to lower constant factors and in-place operation
Deterministic Selection provides guaranteed linear time performance, crucial for real-time systems
Choice depends on application requirements: predictability vs average performance

Data Structures

Arrays excel in random access scenarios (O(1) indexing)
Stacks/Queues are optimal for specific access patterns (LIFO/FIFO)
Linked Lists offer memory flexibility but sacrifice random access performance

Performance Analysis
Time Complexity Summary
Algorithm/OperationBest CaseAverage CaseWorst CaseRandomized QuickselectO(n)O(n)O(n²)Deterministic SelectionO(n)O(n)O(n)Array AccessO(1)O(1)O(1)Array Insert/DeleteO(1)O(n)O(n)Stack Push/PopO(1)O(1)O(1)Queue Enqueue/DequeueO(1)O(1)O(1)Linked List InsertO(1)O(1)O(1)Linked List SearchO(1)O(n)O(n)
Requirements

Python 3.6 or higher
No external dependencies required (uses only standard library)

Testing
All implementations include built-in test cases and error handling for:

Empty data structures
Invalid indices
Duplicate elements
Edge cases (single element, boundary conditions)

Real-World Applications
Selection Algorithms

Database percentile queries
Top-k problem solving
Sensor data analysis
Machine learning feature selection

Data Structures

Arrays: Lookup tables, image processing buffers
Stacks: Function call management, undo operations
Queues: Task scheduling, breadth-first search
Linked Lists: Music playlists, browser history

Future Enhancements

Implement doubly linked lists
Add rooted tree structures
Extend performance analysis with larger datasets
Implement additional selection algorithms (e.g., Introselect)
