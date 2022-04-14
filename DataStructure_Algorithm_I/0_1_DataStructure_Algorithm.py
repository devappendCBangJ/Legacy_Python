"""
● 알고리즘
    0. Divide and Conquer Method
        1) divide step : 큰 문제를 작은 문제로 쪼개서 각각 해결
        2) conquer step : 작은 문제를 큰 문제로 합치면서 해결
        - 알고리즘 측면에서 자주 쓰이는 방법
    1. Sorting1
        1) Merge Sort
            (1) 개념 : sort + merge 반복
                - 각 그룹의 첫 번째 데이터부터 더 작은 것 하나씩 뽑아서 정렬
                ▶강의자료 참조
            (2) Divide and Conquer Method
                1] devide step : array를 2등분. 1개가 될때까지 반복적 쪼개기
                2] conquer step : 쪼개진 1개를 2조각씩 합치기
                ▶강의자료 참조
            (3) 구현 in C언어
                void mergeSort(int a[], int low, int high){
                    if(low < high){
                        int mid = (low+high)/2;

                        mergeSort(a, low, mid);
                        mergeSort(a, mid+1, high);

                        merge(a, low, mid, high);
                    }
                }
            (4) 예제
                ▶강의자료 참조
                ▶강의자료 참조
        2)
        3)
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
                    배열 2등분 반복 + 2등분된 조각들 sorting하면서 merge
                2] 알고리즘
                    [1] 배열 2등분 반복
                    [2] 2등분된 배열 조각들끼리 원소들간 비교 + merge 반복
                    - 정렬 : 조각조각 정렬 + merge
                3] 특징
                    [1] 시간복잡도 : O(nlogn)
                    [2] not inplace : 추가 메모리 사용o
                    [3] stable : 동점자 처리 시 서로의 순서 유지
            (2) Quick Sort
                1] 개념
                    pivot 선택 + 구역 구분 + 2등분 반복
                2] 알고리즘
                    [1] pivot 선택
                    [2] 스왑을 통해 pivot보다 작은 숫자 구역, pivot보다 큰 숫자 구역 구분
                    [3] pivot도 본인 위치로 스왑
                    [4] pivot 기준 배열 2등분
                    [5] 반복
                    [6] merge
                    - 정렬 : 조각조각 내어 결국 정렬
                3] 특징
                    [1] 시간복잡도 : O(n^2)
                        - average : O(nlogn)
                    [2] inplace : 추가 메모리 사용x
                    [3] not stable : swap 사용 - 동점자 처리 시 순서 바꿀수 있으므로 not stable
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