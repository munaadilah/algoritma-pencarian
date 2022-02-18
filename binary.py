def binarySearch(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, low, mid - 1, x)
        else:
            return binarySearch(arr, mid + 1, high, x)

    else:
        return -1

arr = [9, 7, 1, 21, 90, 10, 5, 13, 89, 99, 4]

result = binarySearch(arr, 0, len(arr)-1, 10)

if result != -1:
    print("Elemen ketemu diindeks", str(result))
else:
    print("Elemen tidak ada didalam array")