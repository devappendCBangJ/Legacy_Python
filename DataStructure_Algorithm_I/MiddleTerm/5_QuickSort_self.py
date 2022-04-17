import time

def quick_sort(arr):
    def sort(low, high):
        if(low < high): # low와 high가 같아지는 경우 : 배열에 원소가 1개만 있을때 ♣
            # pivot보다 작은 숫자 구역, pivot보다 큰 숫자 구역별 원소 분류. reculsive하게 반복(pivot 자체는 sorting에 참여 x)
            pivot_idx = partition(low, high)

            # 배열 2등분 reculsive하게 반복
            sort(low, pivot_idx - 1)
            sort(pivot_idx + 1, high)

    def partition(low, high):
        pivot = arr[low] # pivot 선택
        m = low # S1, S2가 비워진 상태에서 시작

        for k in range(low + 1, high + 1): # pivot보다 큰 인덱스부터 시작해서, 마지막 인덱스까지 순회 ♣
            if(arr[k] < pivot): # case2(pivot보다 더 작은 원소인 경우) : swap o, case1(pivot보다 더 큰 원소인 경우) : swap x
                m += 1
                arr[k], arr[m] = arr[m], arr[k]
            else:
                pass
        arr[low], arr[m] = arr[m], arr[low] # pivot 위치로 swap o
        return m

    return sort(0, len(arr) - 1)

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
    quick_sort(arr)
    end = time.time_ns()
    tot_time += (end - start)
tot_time = tot_time / 1000000000 / repeat # ns로 계산했으므로 초단위로 변경. repeat만큼 반복했으므로 1회 평균 계산

# 출력
print("ㅡㅡㅡㅡㅡSorted array isㅡㅡㅡㅡㅡ")
for i in range(len(arr)):
    print("[%04d] %s " %(i, arr[i]), end = "\n")
print(f"{tot_time:.7f} sec")