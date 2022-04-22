"""
○ 알고리즘
    ● Sorting
        0. Divide and Conquer Method
            1) divide step : 큰 문제를 작은 문제로 쪼개서 각각 해결(reculsive)
            2) conquer step : 작은 문제를 큰 문제로 합치면서 해결
            - 알고리즘 측면에서 자주 쓰이는 방법
        1. Sorting 종류
            1) Comparison Based Sort - Iterative Based Sort
                (1) Bubble Sort
                    1] 개념
                        앞뒤 원소 비교 + 스왑
                    2] 알고리즘
                        [1] 앞뒤 원소 비교
                        [2] 스왑
                            0(처음 인덱스) ~ N-1(마지막 인덱스까지의 원소들)
                            0(처음 인덱스) ~ N-2(정렬된 원소를 제외한 원소들)
                            0 ~ N-3 ...
                        [3] 반복
                        - 정렬 : 마지막 인덱스부터 정렬
                    3] 특징
                        [1] 시간복잡도 : O(n^2)
                        [2] inplace : 추가 메모리 사용x
                        [3] stable : 동점자 처리 시 서로의 순서 유지
                (2) Insert Sort
                    1] 개념
                        원소 선택 + 앞쪽 덩어리에서 순서에 맞게 배치
                    2] 알고리즘
                        [1] 1개 원소 선택
                        [2] 해당 원소 앞쪽 덩어리 원소들과 비교
                        [3] 밀어내기
                        [4] 반복
                        - 정렬 : 선택한 원소의 앞쪽 덩어리 내에서 정렬
                        - 밀어내기 : 앞쪽 덩어리의 마지막 원소부터 처음 원소 순으로 비교
                    3] 특징
                        [1] 시간복잡도 : O(n^2)
                        [2] inplace : 추가 메모리 사용x
                        [3] stable : 동점자 처리 시 서로의 순서 유지
                (3) Selection Sort
                    1] 개념
                        최소값부터 정렬
                    2] 알고리즘
                        [1] 앞뒤 원소 비교 반복
                        [2] 최소값 찾기
                        [3] 다 돌면 스왑
                        [4] 반복
                        - 정렬 : 첫 인덱스부터 정렬
                    3] 특징
                        [1] 시간복잡도 : O(n^2)
                        [2] inplace : 추가 메모리 사용x
                        [3] not stable : swap 사용 - 동점자 처리 시 순서 바꿀수 있으므로 not stable
            2) Comparison Based Sort - Recursive Based Sort
                (1) Merge Sort
                    1] 개념
                        배열 2등분 반복(1개로 쪼개질때까지 reculsive) + 2등분된 조각들 비교하여 sorting하면서 merge 반복
                    2] 알고리즘(devide and conquer)
                        [1] 배열 2등분 반복(1개로 쪼개질때까지 reculsive)
                        [2] 2등분된 배열 조각들끼리 원소들간 비교 + sorting + merge 반복
                        - 정렬 : 조각조각 정렬 + merge
                    3] 특징
                        [0] devide and conquer 방식
                        [1] 시간복잡도 : O(nlogn)
                            1]] merge 1회(1 depth)
                                - 총 원소 개수 n = high - low + 1
                                - 비교 <= n - 1 ♣ 왜 이건지는 모르겠다
                                - 기존배열에서 임시 배열로 이동 = n
                                - 임시배열에서 기존 배열로 이동 = n
                                >> O(3n-1) = O(n)
                            2]] merge 횟수(전체 depth)... 시간복잡도가 이것에 의존적 ♣
                                >> O(logn)
                            3]] 총 시간 복잡도
                                >> O(nlogn) = O(n) x O(logn)
                        [2] not inplace : 추가 메모리 사용o
                        [3] stable : 동점자 처리 시 서로의 순서 유지

                        [1] 장점
                            1]] 동일한 속도 : original 배열의 순서에 관계없이 항상 동일한 속도
                            2]] 빠른 속도 : 매우 많은 원소에 유용
                        [2] 단점
                            1]] 구현 어려움
                            2]] not inplace : merge 과정에서 O(n) 수준 추가 메모리 사용
                    4] 구현 in C언어
                        // 전체 함수
                        void mergeSort(int a[], int low, int high){
                            if(low < high){ // low와 high가 같아지는 경우 : 배열에 원소가 1개만 있을때 ♣
                                // 배열 2등분 reculsive하게 반복
                                int mid = (low+high)/2;
                                mergeSort(a, low, mid);
                                mergeSort(a, mid+1, high);

                                // 2등분된 배열 조각들끼리 원소들간 비교 + sorting + merge 반복
                                merge(a, low, mid, high);
                            }
                        }

                        // merge 함수
                        void merge(int a[], int low, int mid, int high){
                            int n = high - low + 1; // 배열 원소 개수
                            int* b = new int[n]; // 임시 배열
                            int left = low, right = mid + 1, bIdx = 0; // 초기값

                            while(left <= mid && right <= high){ // 배열 절반 쪼갬. 두 배열끼리 첫번째 인덱스부터 비교. 작은 것을 임시배열에 담음
                                if(a[left] <= a[right])
                                    b[bIdx++] = a[left++];
                                else
                                    b[bIdx++] = a[right++];
                            }
                            while(left <= mid) b[bIdx++] = a[left++]; // 두 배열 중 한 배열이 남으면 전부 순서대로 임시배열에 담음
                            while(right <= high) b[bIdx++] = a[right++];

                            for(int k = 0; k < n; k++) // 임시 배열 원소를 기존 배열로 붙여넣기
                                a[low+k] = b[k];
                            delete [] b; // 임시배열 삭제
                        }
                (2) Quick Sort
                    1] 개념
                        pivot 선택 + 구역에 맞게 분류 + 2등분 반복
                    2] 알고리즘
                        [1] pivot 선택
                        [2] 스왑을 통해 pivot보다 작은 숫자 구역, pivot보다 큰 숫자 구역별 원소 분류(pivot 자체는 sorting에 참여 x)
                        [3] pivot도 본인 위치로 스왑
                        [4] pivot 기준 배열 2등분
                        [5] 반복
                        [6] merge
                        - 정렬 : 조각조각 내면서 분류하여, 결국 정렬
                    3] 특징
                        [0] devide and conquer 형식
                        [1] 시간복잡도 : 최악 : O(n^2) / average : O(nlogn)
                            1]] partition 1회(1 depth)
                                - 총 원소 개수 n = high - low
                                >> O(n)
                            2]] partition 횟수(전체 depth)... 시간복잡도가 이것에 의존적 ♣
                                - 배열이 이미 오름차순 정렬 되어있음 + pivot으로 첫번째 원소를 사용
                                >> O(n)
                                - pivot으로 분류할때마다 pivot에 의해 두개의 구역이 정확히 반으로 갈라짐
                                >> O(logn)
                            3]] 총 시간 복잡도
                                - 배열이 이미 오름차순 정렬 되어있음 + pivot으로 첫번재 원소를 사용
                                >> O(n^2)
                                - pivot으로 분류할때마다 pivot에 의해 두개의 구역이 정확히 반으로 갈라짐
                                >> O(nlogn)
                        [2] inplace : 추가 메모리 사용x
                        [3] not stable : swap 사용 - 동점자 처리 시 순서 바꿀수 있으므로 not stable
                    4] 구현 in C언어
                        // 전체 함수
                        void quickSort(int a[], int low, int high){
                            if(low < high){ // low와 high가 같아지는 경우 : 배열에 원소가 1개만 있을때 ♣
                                // pivot보다 작은 숫자 구역, pivot보다 큰 숫자 구역별 원소 분류. reculsive하게 반복(pivot 자체는 sorting에 참여 x)
                                int pivotIdx = partition(a, low, high); // 아무거나 선택하면 된다

                                // 배열 2등분 reculsive하게 반복
                                quickSort(a, low, pivotIdx - 1);
                                quickSort(a, pivotIdx + 1, high);
                            }
                        }

                        // partition 함수
                        int partition(int a[], int i, int j){
                            int p = a[i]; // pivot 선택
                            int m = i; // S1, S2가 비워진 상태에서 시작

                            for(int k = i + 1; k <= j; k++){ // pivot보다 큰 인덱스부터 시작해서, 마지막 인덱스까지 순회 ♣
                                if(a[k] < p){ // case2(pivot보다 더 작은 원소인 경우) : swap o
                                    m++;
                                    swap(a[k], a[m]);
                                }
                                else{ // case1(pivot보다 더 큰 원소인 경우) : swap x
                                }
                            }
                            swap(a[i], a[m]); // pivot
                            return m;
                        }
            3) Not Comparison Based Sort
                (1) Bucket Sort
                    1] 개념
                        bucket으로 나누어 각각 정렬
                    2] 알고리즘
                        [1] bucket 기준 선택 + 배열 생성
                        [2] bucket에 원소 담기
                        [3] bucket 내에서 각각 정렬
                            - bucket 내에서 comparison 존재할 수 있다.
                        [4] merge
                    3] 특징
                        [1] 시간복잡도 : ???
                        [2] not inplace : 추가 메모리 사용o
                        [3] ???
                (2) Radix Sort
                    1] 개념
                        각 자리 숫자에 대한 grouping 반복
                    2] 알고리즘
                        [1] 최대 자릿수인 원소 찾기
                        [2] 최대 자릿수만큼 아래의 과정 반복
                        [3]
                    3] 특징
                        [1] 시간복잡도 : O(dn)
                            - d가 작은 경우 : O(n) 수준
                            - 대부분 경우 : O(nlogn) 수준
                        [2] not inplace : 추가 메모리 사용o
                        [3] stable : 동점자 처리 시 서로의 순서 유지

                        [1] 몇째 자리부터 grouping 해야하는지는 상관x
                    4] 구현 in C언어
                        // v : 데이터 담긴 배열
                        // digit : 데이터 특정 자리수의 값
                        // digitQueue : 데이터 특정 자리수의 값을 인덱스로 하는 임시 배열
                        // power : 숫자의 자리수 지정
                        // d : 데이터의 최대 자리수

                        // 전체 함수
                        void radixSort(vector<int> &v, int d){
                            int power = 1; // 1의 자리부터 분류 시작
                            queue<int> digitQueue(10); // 10자리 임시배열

                            for(int i = 0; i < d; i++){
                                distribute(v, digitQueue, power); // 데이터 그룹화 by power
                                collect(digitQueue, v); // 데이터 재결합
                                power *= 10; // power 증가
                            }
                        }

                        // distribute 함수
                        void distribute(vector<int> &v, queue<int> digitQ(), int power){ // 데이터의 특정 자리값 판별 후 임시배열의 그에 맞는 index에 데이터 넣음
                            int digit;
                            for(int i = 0; i < v.size(); i++){
                                digit = (v[i]/power) % 10; // 1의 자리부터 시작
                                digitQ[digit].push(v[i]);
                            }
                        }

                        // collect 함수
                        void collect(queue<int> digitQ[], vector<int> &v){ // 임시벡터의 데이터를 digit이 작은 순서부터 v배열에 다시 넣음
                            int i = 0;
                            int digit;

                            for(digit = 0; digit < 10; digit++){
                                while(!digitQ[digit].empty()){
                                    v[i] = digitQ[digit].front();
                                    digitQ[digit].pop();
                                    i++;
                                }
                            }
                        }
        2. Sorting 요약
            종류 : Worst Case / Best Case / Inplace / stable
            Bubble Sort : O(n^2) / O(n^2) / yes / yes ♣♣♣ 스왑 있는데 stable 맞나???
            Bubble Sort2 : O(n^2) / O(n) / yes / yes
            Insertion Sort : O(n^2) / O(n) / yes / yes ♣♣♣ temp에 insert할 원소 넣어두는데 inplace 맞나???
            Selection Sort : O(n^2) / O(n^2) / yes / no

            Merge Sort : O(nlogn) / O(nlogn) / no / yes
            Quick Sort : O(n^2) / O(nlogn) / yes / no

            Radix Sort : O(dn) / O(dn) / no / yes

    1. Recursion
        1) 개념 : method가 자기 자신을 call
        2) case
            (1) base case : 재귀 호출 없이 답 추출 가능한 경우
                - base case에 대한 정의가 중요하다
                - 항상 base case로 도달해야함(무한 루프에 빠지면 안된다)
            (2) recursive case : 재귀 호출을 써야 답 추출 가능한 경우
        3) 예시
            (1) factorial
                1] 개념
                    n! = 1 * 2 * 3 *... * (n-1) * n
                2] 함수 정의
                    f(n) = 1            if n=0
                    f(n) = n * f(n-1)   else
                3] 코드 구현
                    def factorial(n):
                        if n == 0:
                            return 1
                        else:
                            return n * factorial(n-1)
            (2) english ruler
                1] 개념 : 눈금자 그리기
                2] 일부 구현
                    drawTicks(length)
                        if(length > 0) then
                            drawTicks(length - 1)
                            주어진 길이의 tick을 draw
                            drawTicks(length - 1)
                3] 전체 구현
                    # 선 그리기
                    def draw_line(tic_length, tick_label = ''):
                        line = '-' * tick_length
                        if tick_label:
                            line += ' ' + tick_label
                        print(line)

                    # recursive
                    def draw_interval(center_length):
                        if center_length > 0:
                            draw_interval(center_length - 1)
                            draw_line(center_length)
                            draw_interval(center_length - 1)

                    # 전체 함수
                    def draw_ruler(num_inches, major_length):
                        draw_line(major_length, '0') # 0 표시
                        for j in range(1, 1 + num_inches):
                            draw_interval(major_length - 1)
                            draw_line(major_length, str(j)) # 1, 2, 3,... 표시
            (3) binary search
                1] 개념 : 정렬되어있는 list에서 원소 탐색
                2] 알고리즘
                    target == data[mid] : target 찾기 완료
                    target < data[mid] : mid 앞 덩어리 recur
                    target > data[mid] : mid 뒷 덩어리 recur
                3] 전체 구현
                    def binary_search(data, target, low, high):
                        if low > high:
                            return False
                        else:
                            mid = (low + high) // 2
                            if target == data[mid]:
                                return True
                            elif target < data[mid]:
                                return binary_search(data, target, low, mid-1)
                            else:
                                return binary_search(data, target, mid+1, high)
                4] 특징
                    [1] 시간복잡도 : O(logn)
                        1회 비교 시 수행시간 # 뭔소리??? ♣
                        (mid-1)-low+1 = (low+high)/2-low <= (high-low+1)/2
                        high-(mid+1)+1 = high-(low+high)/2 <= (high-low+1)/2
        4) 종류
            (1) linear recursion
                1] case
                    [1] base case : 재귀 호출 없이 답 추출 가능한 경우
                        - base case에 대한 정의가 중요하다
                        - 항상 base case로 도달해야함(무한 루프에 빠지면 안된다)
                    [2] recursive case : 재귀 호출을 써야 답 추출 가능한 경우
                        - 항상 base case로 도달해야함(무한 루프에 빠지면 안된다)
                        - 재귀적 호출 중 어떤 호출이 필요한지 테스트 할 수 있지만, 궁극적으로 하나의 재귀 호출만 수행해야함
                2] 예시
                    [1] linear sum
                        1]] 알고리즘
                            Algorithm LinearSum(A, n):
                                # A : 배열
                                # n : 원소 개수
                                # output : 배열에서 n번째 원소까지의 합
                                if n = 1 then
                                    return A[0]
                                else
                                    return LinearSum(A, n-1) + A[n-1]
                                    
                            -> for문으로 짜도 된다
                    [2] reverse array
                        1]] 알고리즘
                            Algorithm ReverseArray(A, i, j):
                                # A : 배열
                                # i : 앞쪽에서 오는 원소 인덱스
                                # j : 뒤쪽에서 오는 원소 인덱스
                                # output : 배열 앞 뒤 원소 reverse
                                if i < j then
                                    swap A[i] and A[j]
                                    ReverseArray(A, i+1, j-1)
                                return

                            -> for문으로 짜도 된다
                        2]] 코드 구현
                            def reverse(S, start, stop):
                                if start < stop-1: # 배열 인덱스가 0부터 시작하기 때문에 stop-1이 마지막 원소 인덱스
                                    S[start], S[stop-1] = S[stop-1], S[start]
                                    reverse(S, start+1, stop-1)

                            -> for문으로 짜도 된다
                    [3] power
                        1]] 알고리즘1
                            P(x, n) = x^n

                            P(x, n) = 1                 (if n = 0)
                            P(x, n) = x * p(x, n-1)     (else)

                            -> O(n)
                            -> for문으로 짜도 된다
                        2]] 알고리즘2
                            P(x, n) = 1                     (if x = 0)
                            P(x, n) = x * P(x, (n-1)/2)^2   (if x > 0 is odd)
                            P(x, n) = p(x, n/2)^2           (if x > 0 is even)

                            Algorithm Power(x, n):
                                # x : 밑
                                # n : 지수
                                # output : x^n
                                if n = 0 then
                                    return 1
                                if n is odd then
                                    y = power(x, (n-1)/2)   # O(logn)
                                    return x * y * y
                                else
                                    y = power(x, n/2)       # O(logn)
                                    return y * y

                            -> O(logn)
                            -> for문으로 짜도 된다
            (2) tail recursion
                1] 개념 : last step에서 recursive call 발생
                2] 예시 알고리즘
                    Algorithm IterativeReverseArray(A, i, j):
                        # A : 배열
                        # i : 앞쪽에서 오는 원소 인덱스
                        # j : 뒤쪽에서 오는 원소 인덱스
                        # output : 배열 앞뒤 원소 reverse
                        while i < j do
                            Swap A[i] and A[j]
                            i = i + 1
                            j = j - 1
                        return IterativeReverseArray(A, i, j) # 바로 점프해서 속도 빠를 수 있다.
            (3) binary recursion
                1] 개념 : 각각의 non base case에서 2개 recursive call 발생
                2] 예시 알고리즘
                    [1] english ruler
                        drawTicks(length)
                            if(length > 0) then
                                drawTicks(length - 1)
                                주어진 길이의 tick을 draw
                                drawTicks(length - 1)
                    [2] binary sum
                        Algorithm BinarySum(A, i, n):
                            # A : 배열
                            # i : 배열에서 원소 인덱스
                            # n : 분할되고 남은 원소 개수
                            # output : 배열에서 n번째 원소까지의 합
                            if n = 1 then
                                return A[i]
                            return BinarySum(A, i, n/2) + BinarySum(A, i + n/2, n/2)
                    [3] fibonacci numbers 비효율적 방법
                        F_0 = 0
                        F_1 = 1
                        F_i = F_(i-1) + F_(i-2)         (if i > 1)

                        Algorithm BinaryFib(k):
                            # k : 피보나치 계산 횟수
                            # output : 피보나치 수 = F_k
                            if k = 1 then
                                return k
                            else
                                return BinaryFib(k-1) + BinaryFib(k-2)

                        -> recursion 횟수 : n_k > 2^(k/2)
                    [4] fibonacci numbers 효율적 방법
                        Algorithm LinearFib(k):
                            # k : 피보나치 계산 횟수
                            # output : 피보나치 수 쌍 = F_k, F_(k-1)
                            if k = 1 then
                                return (k, 0)
                            else
                                (i, j) = LinearFib(k-1)
                                return (i+j, i)

                        -> recursion 횟수 : n_k = k-1
            (4) multiple recursion
                1] 개념 : 많은 recursive call 발생(1 or 2번이 아님)
                2] 예시
                    [1] summation puzzles
                        pot + pan = bib     // 421 + 437 = 858 (p=4, o=2, t=1, a=3, n=7, b=8, i=5)
                        dog + cat = pig
                        boy + girl = baby
"""