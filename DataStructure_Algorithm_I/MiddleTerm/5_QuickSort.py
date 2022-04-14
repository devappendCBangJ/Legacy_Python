import time

def quick_sort(arr):
    def sort(low, high):
        if high <= low:
            return
        mid = partition(low, high)
        # pivot 기준 배열 2등분
        sort(low, mid - 2) #
        sort(mid, high)

    def partition(low, high):
        # pivot 선정
        pivot = arr[(low + high) // 2]
        # 스왑을 통해 pivot보다 작은 숫자 구역, pivot보다 큰 숫자 구역 구분
        while low <= high:
            # low 원소가 pivot보다 작은 경우
            while arr[low] < pivot:
                low += 1
            # high 원소가 pivot보다 큰 경우
            while arr[high] > pivot:
                high -= 1
            # low 원소가 pivot이랑 같거나 큰 경우 + high 원소가 pivot이랑 같거나 작은 경우
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1
        return low

    return sort(0, len(arr) - 1)

arr = []
# 메모장 열기
with open('name.txt', 'r') as file:
    line = None
    # 1줄씩 읽고 배열에 넣기
    while line != '':
        line = file.readline()
        arr.append(line.strip('\n'))

start = time.time()
quick_sort(arr)
end = time.time()

# 출력
print("ㅡㅡㅡㅡㅡSorted array isㅡㅡㅡㅡㅡ")
for i in range(len(arr)):
    print("[%04d] %s " %(i, arr[i]), end = "\n")
print(f"{end - start:.7f} sec")