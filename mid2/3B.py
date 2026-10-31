def lower(lst, x):
    l = 0 
    r = len(lst) - 1
    while l <= r:
        m = (l+r) // 2
        if lst[m] < x:
            l = m + 1 
        else:
            r = m - 1
    return l 
def upper(lst, x):
    l = 0
    r = len(lst) - 1
    while l <= r:
        m = (l+r) // 2
        if lst[m] <= x:
            l = m + 1
        else:
            r = m - 1
    return l
