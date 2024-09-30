def buble_sort(lst):
    for j in range(len(lst) - 1, 0, -1):
        i = 0 
        while i < j:
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
            i += 1
    return lst

if __name__ == '__main__':
    from random import randint
    lst = [randint(1, 1000) for _ in range(1000)]
    print(buble_sort(lst))