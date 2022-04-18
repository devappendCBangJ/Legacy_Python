def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if (arr[j] < arr[i - 1]):
                t = arr[j]
                arr[j] = arr[j - 1]
                arr[j - 1] = t
            else:
                break
            i = i - 1
    return arr

def merge(arr1, arr2):
    a = 0
    b = 0
    arr3 = []

    while(a < len(arr1) and b < len(arr2)):
        if(arr1[a] < arr2[b]):
            arr3.append(arr1[a])
            a = a + 1
        elif(arr1[a] > arr2[b]):
            arr3.append(arr2[b])
            b = b + 1
        else:
            arr3.append(arr1[a])
            arr3.append(arr2[b])
            a = a + 1
            b = b + 1
    while(a < len(arr1)):
        arr3.append(arr1[a])
        a = a + 1
    while(b < len(arr2)):
        arr3.append(arr2[b])
        b = b + 1

    return arr3

def tim_sort():
    for x in range(0, len(arr), run):
        arr[x : x + run] = insertion_sort(arr[x : x + run])
    runinc = run
    while(runinc < len(arr)):
        for x in range(0, len(arr), 2 * runinc):
            arr[x : x + 2 * runinc] = merge(arr[x : x + runinc], arr[x + runinc : x + 2 * runinc])
        runinc = runinc * 2

arr = [3, 30, 23, 35, 8, 10, 40, 55, 50, 52]
run = 5
tim_sort()
print(arr)