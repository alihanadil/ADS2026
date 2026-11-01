def sift_down(h, i, n):
    temp = h[i]
    curr = i 
    while True:
        l = 2*i + 1
        r = l + 1
        if l >= n: break 
        if r < n and h[r] > h[l]:
            maxid = r 
        else:
            maxid = l 
        if h[maxid] > temp:
            h[curr] = h[maxid]
            curr = maxid 
        else:
            break
    h[curr] = temp 
def sift_up(h, i):
    temp = h[i]
    curr = i 
    while curr > 0:
        p = (curr - 1) // 2 
        if h[p] < temp:
            h[curr] = h[p]
            curr = p 
        else:
            break 
    h[curr] = temp