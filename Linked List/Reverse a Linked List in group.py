def reverse(head, k):
    h = head
    prev = None
    cur = None
    c = 0
    while head and c<k:
        cur = head.next
        head.next = prev
        prev = head
        head = cur
        c+=1
    if cur:
        h.next = reverse(cur,k)
    return prev
