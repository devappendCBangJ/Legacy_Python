"""
● Data Structure vs Algorithm
    1. Data Structure
        1) Primitive Data Structure
            (1)
                1] int
                2] char
                3] float
                4] double
        2) Non-Primitive Structure
            (1) Linear
                1] Array
                2] Stacks
                3] Queues
                4] (Linked)List
            (2) Non-Linear
                1] Tree
                2] Graphs
    2. Algorithm
        1) ##Concept : define how to process data in order to get the expected results
            - input >> Algorithm >> output
        2) ##Characteristics
            (1) Every step : clear, unambiguous
            (2) data : well defined
            (3) feasible (completion & understandable / readable)
        3) Algorithm Analysis
            (1) Running Time
                1] Seven Functions
                    [1] 1 : constant
                    [2] logn : logarithmic
                    [3] n : linear
                    [4] nlogn : N-Log-N
                    [5] n^2 : quadratic
                    [6] n^3 : cubic
                    [7] 2^n : exponential
                2] Counting Primitive Operations
                    [1] Big-Oh Notation(최악)
                        - f(n) <= cg(n) for n >= n_0
                        - Drop lower-order terms
                        - Drop constant factors
                    [2] Big-Theta(평균)
                        - c' g(n) <= f(n) <= c'' g(n) for n >= n_0
                    [3] Big-Omega(최선)
                        - f(n) >= cg(n) for n >= n_0
            (2) Pseudocode
                1] high level description
                2] Evaluate algorithm indepent of the SW/HW
    3. Object Oriented Programming
        1) Object
            (1) ##created : instance of a class
            (2) ##contains : property & method
        2) Object-Oriented Design Principles
            (1) ##Characteristics
                1] Modularity
                2] Abstraction
                3] Encapsulation
            (2) ##Process
                1] Class define : porperty & method define
                2] Constructors(생성자) : create instance
                3] Operator Overloading : provide natural senmantics for many operations
                4] Iterators : provide repeated operations
                    - __next__ : return next element
                    - StopIteration : if there are no further elements, raise StopIteration

                    - __len__ : return number of entries
                    - __getitem__ : return index k
                5] Inheritance
                    [1] base class : existing class
                    [2] subclass = child class : newly defined class

● Data Structure Kind
    1. Recursive method
        1) ##Concept : call 반복 >> return 반복
            def factorial(n):
                if n == 0:
                    return 1
                else:
                    return n * factorial(n-1)
        2) ##ex
            (1) Binary Search
                1] ##Conditions
                    - Data : ordered form
                2] ##Concept : half & half reduce search
                3] ##Characteristics
                    [1] Big-Oh : O(logn)
"""
