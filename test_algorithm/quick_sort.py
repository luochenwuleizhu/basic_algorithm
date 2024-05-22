# 在快速排序中，我们选择一个基准元素，然后将数组分成三部分：小于基准的部分、等于基准的部分和大于基准的部分。
# 接着对小于和大于基准的部分递归地应用快速排序，最终合并各部分得到排序后的数组。
# 快速排序的时间复杂度为 O(nlogn)，是一种高效的排序算法。
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # 选择基准元素
    left = [x for x in arr if x < pivot]  # 分区：小于基准的元素
    middle = [x for x in arr if x == pivot]  # 分区：等于基准的元素
    right = [x for x in arr if x > pivot]  # 分区：大于基准的元素

    return quick_sort(left) + middle + quick_sort(right)

# 示例用法
arr = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
if __name__ == "__main__":
    sorted_arr = quick_sort(arr)
    print(sorted_arr)
