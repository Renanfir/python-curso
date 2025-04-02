def mergedSortedArrays(arr1, arr2):
    arr3 = []
    for i in arr1:
        arr3.append(i)

    for i in arr2:
        arr3.append(i)

    arr3.sort()
    print(arr3)


a = [0,3,4,31]
b = [4,6,30]

mergedSortedArrays(a,b)




