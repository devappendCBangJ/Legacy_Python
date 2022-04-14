# https://www.daleseo.com/sort-insertion/

import time

def insert_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]

# 삽입 정렬
# def insertSort(arr):
#     for i in range(1, len(arr)):
#         temp = arr[i]
#         for j in range(i-1, 0, -1):
#             if arr[j] > temp:
#                 arr[j+1] = arr[j]
#             else:
#                 arr[j+1] = temp
#                 break
#         arr[0] = temp

arr = []
# 메모장 열기
with open('name.txt', 'r') as file:
    line = None
    # 1줄씩 읽고 배열에 넣기
    while line != '':
        line = file.readline()
        arr.append(line.strip('\n'))

start = time.time()
insert_sort(arr)
end = time.time()

# 출력
print("ㅡㅡㅡㅡㅡSorted array isㅡㅡㅡㅡㅡ")
for i in range(len(arr)):
    print("[%04d] %s " %(i, arr[i]), end = "\n")
print(f"{end - start:.7f} sec")