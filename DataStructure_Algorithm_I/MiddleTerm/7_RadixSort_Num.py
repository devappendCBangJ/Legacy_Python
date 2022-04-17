# https://devjin-blog.com/sort-algorithm-9/

import time

class radix_sort:
    def __init__(self, num):
        self.num = num

    def radix_sort(self):
        # 가장 큰 수 추출
        max1 = max(self.num)

        # 1의 자리부터 차수 높이면서 sorting
        exp = 1
        while max1 / exp > 0:
            self.count_sort(self.num, exp)
            exp *= 10

    def count_sort(self, A, k):
        # B : sorting된 원소 담는 배열
        B = [0] * len(A)
        # C : 0~9 숫자 개수 배열
        C = [0] * (10)

        # C : 0~9 숫자 개수 계산
        for i in range(0, len(A)):
            index = (A[i] // k)
            C[(index) % 10] += 1 # 1의 자리부터 차수 높이면서 sorting

        # C : 0~9 숫자 개수 누적합 계산 -> B 배열에 sorting할 때, 해당 숫자가 어느 위치에 들어가야할지 파악 가능. 인덱스 뒤쪽부터 정렬해서 현재 자리수에서 같은 수를 가질때, 이전 자리수가 더 큰 자료를 더 높은 인덱스에 둘 수 있게 만듦
        for i in range(1, 10):
            C[i] += C[i - 1]

        # B : sorting된 원소 담음. C가 B의 인덱스를 알려줌
        i = len(A) - 1 # 0~len(A)-1로, len(A)개를 표현 하기 위해. 인덱스 뒤쪽부터 정렬해서 현재 자리수에서 같은 수를 가질때, 이전 자리수가 더 큰 자료를 더 높은 인덱스에 둘 수 있게 만듦
        print("C :", C)
        print("B :", B)
        while i >= 0:
            index = (A[i] // k)
            B[C[(index) % 10] - 1] = A[i] # B배열의 인덱스 0번부터 값을 넣기 위해. 인덱스 뒤쪽부터 정렬해서 현재 자리수에서 같은 수를 가질때, 이전 자리수가 더 큰 자료를 더 높은 인덱스에 둘 수 있게 만듦
            C[(index) % 10] -= 1 # 인덱스 뒤쪽부터 정렬해서 현재 자리수에서 같은 수를 가질때, 이전 자리수가 더 큰 자료를 더 높은 인덱스에 둘 수 있게 만듦
            print("C :", C)
            print("B :", B)
            i -= 1

        # 기존 리스트에 복사를 한다
        for i in range(len(A)):
            A[i] = B[i]

 # Average Filter : 실행 시간 계속 달라지므로 여러번 반복하여 평균 취함
tot_time = 0
repeat = 500
for i in range(repeat):
    arr = []
    # 메모장 열기
    with open('name.txt', 'r') as file:
        line = None
        # 1줄씩 읽고 배열에 넣기
        while line != '':
            line = file.readline()
            arr.append(line.strip('\n'))
    # 시간 측정
    start = time.time_ns()
    radix_sort(arr)
    end = time.time_ns()
    tot_time += (end - start)
tot_time = tot_time / 1000000000 / repeat # ns로 계산했으므로 초단위로 변경. repeat만큼 반복했으므로 1회 평균 계산

# 출력
print("ㅡㅡㅡㅡㅡSorted array isㅡㅡㅡㅡㅡ")
for i in range(len(arr)):
    print("[%04d] %s " %(i, arr[i]), end = "\n")
print(f"{tot_time:.7f} sec")