# https://stackabuse.com/bucket-sort-in-python/

import time

def bucket_sort(input_list):
    # bucket list의 size 범위 설정
    size = 26

    # input list와 크기가 같은 2차원 bucket list 생성(bucket의 크기를 input list의 크기와 같은 것을 사용하겠다!)
    buckets_list = []
    for x in range(size):
        buckets_list.append([]) # [[], [], [], [], []]꼴 2차원 배열 생성
    # print(buckets_list) # 확인용 코드

    # 해당 bucket list에 input list의 원소 분류
    for i in range(len(input_list)):
        # print(input_list[i]) # 확인용 코드
        for j in range(len(input_list[i])):
            # 담아야할 bucket의 index
            # print(input_list[i][j]) # 확인용 코드
            if(j == 0):
                k = (ord(input_list[i][j]) - 65) % 26
            else:
                k = (ord(input_list[i][j]) - 97) % 26
            buckets_list[k].append(input_list[i])
        # print(buckets_list) # 확인용 코드

    # bucket list별로 삽입 정렬
    for z in range(len(buckets_list)): # len(input_list) = len(buckets_list) : input list의 개수와 buckets list의 개수를 같게 생성했으므로 이렇게 써도 된다
        insertion_sort(buckets_list[z])

    # bucket list의 결과 합치기
    final_output = []
    for x in range(len(buckets_list)): # len(input_list) = len(buckets_list) : input list의 개수와 buckets list의 개수를 같게 생성했으므로 이렇게 써도 된다
        final_output = final_output + buckets_list[x]
    return final_output

def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        for j in range(i, 0, -1):
            if bucket[j - 1] > bucket[j]:
                bucket[j - 1], bucket[j] = bucket[j], bucket[j - 1]

arr = []
# 메모장 열기
with open('name.txt', 'r') as file:
    line = None
    # 1줄씩 읽고 배열에 넣기
    while line != '':
        line = file.readline()
        arr.append(line.strip('\n'))

start = time.time()
arr = bucket_sort(arr)
end = time.time()

# 출력
print("ㅡㅡㅡㅡㅡSorted array isㅡㅡㅡㅡㅡ")
for i in range(len(arr)):
    print("[%04d] %s " %(i, arr[i]), end = "\n")
print(f"{end - start:.7f} sec")