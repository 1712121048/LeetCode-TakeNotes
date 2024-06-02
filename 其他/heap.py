def heapify(arr, n, i):
    """
    将数组arr中的元素进行堆化处理。
    :param arr: 待排序数组
    :param n: 数组长度
    :param i: 当前需要堆化的节点索引
    """
    largest = i        # 初始化为当前节点
    left = 2 * i + 1   # 左子节点
    right = 2 * i + 2  # 右子节点

    # 如果左子节点存在且大于当前节点
    if left < n and arr[left] > arr[largest]:
        largest = left

    # 如果右子节点存在且大于当前节点
    if right < n and arr[right] > arr[largest]:
        largest = right

    # 如果当前节点不是最大
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # 交换
        heapify(arr, n, largest)  # 递归堆化受影响的子树

def heap_sort(arr):
    """
    对数组进行堆排序。
    :param arr: 待排序数组
    """
    n = len(arr)

    # 构建最大堆
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # 一个一个从堆顶取出元素并调整堆
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 交换
        heapify(arr, i, 0)  # 重新调整堆

# 示例用法
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("排序前的数组:", arr)
    heap_sort(arr)
    print("排序后的数组:", arr)
