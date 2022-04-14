# https://stackabuse.com/bucket-sort-in-python/

import time

def bucket_sort(input_list):
    # 최대 길이인 문자의 개수
    size = len(max(input_list, key = len))
    size = (ord('z') - ord('a')) + 1
    min_base = ord('A') - 1

    # bucket 배열 생성
    buckets_list = []
    for x in range(len(input_list)):
        buckets_list.append([])

    # Put list elements into different buckets based on the size
    for i in range(len(input_list)):
        j = int(input_list[i] / size)
        if j != len(input_list):
            buckets_list[j].append(input_list[i])
        else:
            buckets_list[len(input_list) - 1].append(input_list[i])

    letter = ord(item[col]) - min_base if col < len(item) else 0  # 현재 원소 길이 > 확인하고 싶은 문자열 인덱스 : 숫자 개수 count++, 현재 원소 길이 < 확인하고 싶은 문자열 인덱스 : 숫자 개수 0
    count[letter] += 1

    # Sort elements within the buckets using Insertion Sort
    for z in range(len(input_list)):
        insertion_sort(buckets_list[z])

    # Concatenate buckets with sorted elements into a single list
    final_output = []
    for x in range(len(input_list)):
        final_output = final_output + buckets_list[x]
    return final_output

def insertion_sort(bucket):
    for i in range (1, len (bucket)):
        var = bucket[i]
        j = i - 1
        while (j >= 0 and var < bucket[j]):
            bucket[j + 1] = bucket[j]
            j = j - 1
        bucket[j + 1] = var

arr = []
# 메모장 열기
with open('name.txt', 'r') as file:
    line = None
    # 1줄씩 읽고 배열에 넣기
    while line != '':
        line = file.readline()
        arr.append(line.strip('\n'))

start = time.time()
bucket_sort(arr)
end = time.time()

# 출력
print("ㅡㅡㅡㅡㅡSorted array isㅡㅡㅡㅡㅡ")
for i in range(len(arr)):
    print("[%04d] %s " %(i, arr[i]), end = "\n")
print(f"{end - start:.7f} sec")