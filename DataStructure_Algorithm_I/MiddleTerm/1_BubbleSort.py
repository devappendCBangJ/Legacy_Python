import time

# 버블 정렬
def bubbleSort(arr):
        for i in range(len(arr)):
            for j in range(0, len(arr)-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

arr = []
# 메모장 열기
with open('name.txt', 'r') as file:
    line = None
    # 1줄씩 읽고 배열에 넣기
    while line != '':
        line = file.readline()
        arr.append(line.strip('\n'))

start = time.time()
bubbleSort(arr)
end = time.time()

# 출력
print("ㅡㅡㅡㅡㅡSorted array isㅡㅡㅡㅡㅡ")
for i in range(len(arr)):
    print("[%04d] %s " %(i, arr[i]), end = "\n")
print(f"{end - start:.5f} sec")