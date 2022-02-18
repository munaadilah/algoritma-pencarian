def sequentialSearch(arr, x):
    indeks = 0
    ketemu = False

    while indeks < len(arr) and not ketemu:
        if arr[indeks] == x:
            ketemu = True
        else:
            indeks += 1
    return ketemu, indeks

a = [9, 7, 1, 21, 90, 10, 5, 13, 89, 99, 4]

print(sequentialSearch(a, 21))