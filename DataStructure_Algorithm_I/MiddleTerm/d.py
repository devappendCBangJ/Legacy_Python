import time

def dual_pivot_sort(list, start, top):
    if top <= start:
        return
    p = start
    q = top
    k = p+1
    h = k
    l = q-1
    if list[p] > list[q]:
        list[p], list[q] = list[q], list[p]
    while k <= l:
    # the last non-check index is l,as l+1 to top - 1 is the part III,
    #where all elements > list[top]
        if list[k] < list[p]:
            list[h], list[k] = list[k], list[h]
            #h is the first element of part II
            h += 1
            #increase h by 1, for pointing to the first element of part II
            k += 1
            #increase k by 1, because we have checked list[k]
        elif list[k] > list[q]:
        #l is the last element of part IV
            list[k], list[l] = list[l], list[k]
            #don't increase k, as we have not check list[l] yet
            l -= 1
            #after swap, we should compare list[k] with list[p] and list[q] again
        else: k += 1
        # no swap, then the current k-th value is in part II, thus we plus 1 to k
    h -= 1#now,h is the last element of part I
    l += 1 #now, l is the first element of part III
    list[p], list[h] = list[h], list[p]
    list[q], list[l] = list[l], list[q]
    dual_pivot_sort(list, start, h-1)
    dual_pivot_sort(list, h+1, l-1)
    dual_pivot_sort(list, l+1, top)

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
    dual_pivot_sort(arr, 0, len(arr) - 1)
    end = time.time_ns()
    tot_time += (end - start)
tot_time = tot_time / 1000000000 / repeat # ns로 계산했으므로 초단위로 변경. repeat만큼 반복했으므로 1회 평균 계산

# 출력
print("ㅡㅡㅡㅡㅡSorted array isㅡㅡㅡㅡㅡ")
for i in range(len(arr)):
    print("[%04d] %s " %(i, arr[i]), end = "\n")
print(f"{tot_time:.7f} sec")