# 从前往后两两比较，将较大的元素交换到后面。对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最大的元素会出现在数组末尾。
# 冒泡排序的时间复杂度为 O(n^2)，是一种经典的排序算法。
def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# 示例用法
arr = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
if __name__ == "__main__":
    sorted_arr = bubble_sort(arr)
    print(sorted_arr)
