# 简单选择排序 时间复杂度O(n^2)，空间复杂度O(1)
arr = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr

if __name__ == "__main__":
    print(selection_sort(arr))
