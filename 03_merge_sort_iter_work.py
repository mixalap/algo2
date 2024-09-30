def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    len_left, len_right = len(left), len(right)
    
    while left_idx < len_left and right_idx < len_right:
        # Сравниваем:
        if left[left_idx] <= right[right_idx]:
            # Добавляем в result:
            result.append(left[left_idx])
            # Сдвигаем указатель:
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    
    return result + left[left_idx:] + right[right_idx:]

def merge_sort_iter(array: list):
    lsts = [[x] for x in array]
    while len(lsts) > 1:
        new_lsts = []
        for i in range(0, len(lsts) - 1, 2):
            new_lsts.append(merge(lsts[i], lsts[i + 1]))
        if len(lsts) % 2:
            new_lsts.append(lsts[-1])
        lsts = new_lsts
    return lsts[0]

def merge_sort(array):
    # Сохраняем длину массива в переменную, чтобы не считать её каждый раз.
    len_array = len(array)
    # Базовый случай рекурсии.
    if len_array <= 1:
        return array
    
    # Рекурсивный разбор массива в левой половине:
    # передаём в merge_sort() левую половину полученного на вход массива.
    left = merge_sort(array[0 : len_array // 2])
    
    # Рекурсивный разбор массива в правой половине:
    # передаём в merge_sort() правую половину полученного на вход массива.
    right = merge_sort(array[len_array // 2 : len_array])
    
    return merge(left, right)

if __name__ == '__main__':
    import timeit
    from random import randint
    from tqdm import tqdm

    time_results = []
    step_len = 10000
    steps = 10
    rng = range(step_len, step_len * (steps + 1), step_len)

    for len_arr in tqdm(rng, desc='итерации'):
        test_array = [randint(0, x + x) for x in range(len_arr + 1)]
        start_time = timeit.default_timer()
        merge_sort_iter(test_array)
        time_results.append((
            round(timeit.default_timer() - start_time, 6), len_arr
        ))

    print(time_results)