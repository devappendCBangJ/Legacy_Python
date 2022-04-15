"""
● 알고리즘
    0. Divide and Conquer Method
        1) divide step : 큰 문제를 작은 문제로 쪼개서 각각 해결(reculsive)
        2) conquer step : 작은 문제를 큰 문제로 합치면서 해결
        - 알고리즘 측면에서 자주 쓰이는 방법
    1. Sorting1
        1) Merge Sort
            (1) 개념 : sort + merge 반복
                - 각 그룹의 첫 번째 데이터부터 더 작은 것 하나씩 뽑아서 정렬
            (2) Divide and Conquer Method
                1] devide step : array를 2등분. 1개가 될때까지 반복적 쪼개기
                2] conquer step : 쪼개진 1개를 2조각씩 합치기

    2. Sorting 종류
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
    3. Sorting 요약
        종류 : Worst Case / Best Case / Inplace / stable
        Bubble Sort : O(n^2) / O(n^2) / yes / yes ♣♣♣ 스왑 있는데 stable 맞나???
        Bubble Sort2 : O(n^2) / O(n) / yes / yes
        Insertion Sort : O(n^2) / O(n) / yes / yes ♣♣♣ temp에 insert할 원소 넣어두는데 inplace 맞나???
        Selection Sort : O(n^2) / O(n^2) / yes / no

        Merge Sort : O(nlogn) / O(nlogn) / no / yes
        Quick Sort : O(n^2) / O(nlogn) / yes / no

        Radix Sort : O(dn) / O(dn) / no / yes
"""