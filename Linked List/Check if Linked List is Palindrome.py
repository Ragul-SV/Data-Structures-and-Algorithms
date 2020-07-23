def isPalindrome(head):
    fast = slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    prev = None
    while slow:
        nxt = slow.next
        slow.next = prev
        prev = slow
        slow = nxt
    while prev and head:
        if prev.data!=head.data:
            return False
        prev = prev.next
        head = head.next
    return True
