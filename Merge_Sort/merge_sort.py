def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        i,z,k = 0,0,0
        while i < len(left) and z < len(right):
            if left[i] < right[z]:
                arr[k] = left[i]
                i = i + 1
            else:
                arr[k] = right[z]
                z = z + 1
            k = k + 1

        while i < len(left):
            arr[k] = left[i]
            i = i + 1
            k = k + 1

        while z < len(right):
            arr[k] = right[z]
            z = z + 1
            k = k + 1
        import pdb; pdb.set_trace()

arr = [54,24,34,56,77]
merge_sort(arr)
print(arr)
