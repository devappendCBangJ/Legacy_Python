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
    2. Sorting2
"""