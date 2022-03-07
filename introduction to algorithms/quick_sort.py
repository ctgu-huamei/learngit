def quick_sort(num_list):
    '''
    快速排序算法，
    1，选择一个基准值
    2，将数组分为两个子数组，左侧子数组中的值小于基准值，右侧子数组中的值大于基准值
    3，对这两个子数组重复1，2步骤
    :param num_list:
    :return:
    '''
    if len(num_list) < 2:
        return num_list
    base = num_list[0]
    left = [i for i in num_list[1:] if i <= base]
    right = [i for i in num_list[1:] if i > base]
    return quick_sort(left) + [base] + quick_sort(right)


if __name__ == "__main__":
    nums = [16, 34, 12, 14, 1, 3, 19, 24]
    a = quick_sort(nums)
    print(a)


