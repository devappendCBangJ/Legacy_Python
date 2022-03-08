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
                2] Evaluate algorithm independent of the SW/HW
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

● Data Structure
    1. Kind
        1) Recursive method
            (1) ##Concept : call 반복 >> return 반복
                def factorial(n):
                    if n == 0:
                        return 1
                    else:
                        return n * factorial(n-1)
            (2) ##ex
                1] Binary Search
                    [1] ##Conditions
                        - Data : ordered form
                    [2] ##Concept : half & half reduce search
                    [3] ##Characteristics
                        - Big-Oh : O(logn)

    2. Memory manangement
        1) Computer Architecture(x86)
            (1) 구조
                1] 부품
                    [1] Ports, CD-ROM, Floppy Drive
                    [2] RAM : 주소 저장. 휘발성o
                    [3] ROM : 휘발성x
                    [4] register
                    [5] CPU

                    - speed : HDD < RAM < register
                    - capability : register < RAM < HDD

                2] 로더
                    1] Boot Loader
                    2] Program Loader : ex. excel
                    3] Class Loader : ex. java의 class

                3] CPU
                    CPU <-> RAM

                    - fetch & excute cycle
                    - indexing of current program position
                        1] page faults : page not currently present in RAM
                            -> Use Virtual memory : idealized abstraction of the storage resources
                                Virtual memory <-> Physical memory

    3. List : Array-Based Sequences
        (1) 저장 구조
            1] sequence type : a set of memory locations
                [1] list
                [2] tuple
                [3] str

            2] 저장 방법
                [1] array list
                    1]] char arrays
                        [[1]] elements : store primitive elements
                        [[2]] reference : store references to objects
                    2]] intger arrays
                        [[1]] elements
                        [[2]] reference : 형식으로 저장하는 것보다 주소형태로 저장하는 것이 유리
                [2] linked list
                    
        (2) 활용
            1] insertion
                - 해당 인덱스부터 한칸씩 뒤로 밀음 + 해당 원소 삽입
                - 시간복잡도 : O(n)

                [1] Incremental strategy : size + constant c
                    - n + c + 2c + ... + kc
                    - T(n) = O(n + k^2)
                [2] Doubling strategy : size x2
                    - T(n) = O(n)
            2] remove
                - 해당 원소 제거 + 해당 인덱스 뒤부터 한칸씩 앞으로 당김
                - 시간복잡도 : O(n)

	4. Stack : 

"""
