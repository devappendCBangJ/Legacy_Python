# https://www.daleseo.com/sort-selection/

import time

def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr = []
# 메모장 열기
with open('name.txt', 'r') as file:
    line = None
    # 1줄씩 읽고 배열에 넣기
    while line != '':
        line = file.readline()
        arr.append(line.strip('\n'))

start = time.time()
selection_sort(arr)
end = time.time()

# 출력
print("ㅡㅡㅡㅡㅡSorted array isㅡㅡㅡㅡㅡ")
for i in range(len(arr)):
    print("[%04d] %s " %(i, arr[i]), end = "\n")
print(f"{end - start:.5f} sec")