def binary_search(lst, start, end, target):
    if start >= end:
        return "No match found"
    
    mid_idx = (start + end) // 2
    mid_val = lst[mid_idx]

    if mid_val[ :len(target)] == target:
        return mid_idx
    
    if mid_val[ :len(target)] < target:
        return binary_search(lst, mid_idx + 1, end, target)
    if mid_val[ :len(target)] > target:
        return binary_search(lst, start, mid_idx, target)