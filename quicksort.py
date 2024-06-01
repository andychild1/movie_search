from random import randrange

def quicksort(lst, start, end):
    if start >= end:
        return
    
    mid_idx = randrange(start, end + 1)
    pivot = lst[mid_idx]

    lst[end], lst[mid_idx] = lst[mid_idx], lst[end]

    less_than_ptr = start

    for idx in range(start, end):
        if lst[idx]["title"] < pivot["title"]:
            lst[idx], lst[less_than_ptr] = lst[less_than_ptr], lst[idx]
            less_than_ptr += 1

    lst[end], lst[less_than_ptr] = lst[less_than_ptr], lst[end]

    quicksort(lst, less_than_ptr +1, end)
    quicksort(lst, start, less_than_ptr-1)
