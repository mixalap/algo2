def buble_sort_r(lst):
    def buble_sort(indx):
        if indx <= 0:
            return
        i = 0
        while i < indx:
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
            i += 1
        buble_sort(indx - 1)

    buble_sort(len(lst) - 1)
    return lst


def buble_sort(lst):
    for j in range(len(lst) - 1, 0, -1):
        i = 0 
        while i < j:
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
            i += 1
    return lst

if __name__ == '__main__':
    lst = [3, 4, 5, 0, 1]
    # from random import randint
    # lst = [randint(1, 1000) for _ in range(1000)]
    print(buble_sort_r(lst))
