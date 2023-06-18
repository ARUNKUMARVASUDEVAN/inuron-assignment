class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy = ListNode(0)  # Dummy node to simplify the code
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        # Calculate the sum of current digits and the carry
        digit_sum = carry
        if l1:
            digit_sum += l1.val
            l1 = l1.next
        if l2:
            digit_sum += l2.val
            l2 = l2.next

        # Update the carry and create a new node with the sum digit
        carry = digit_sum // 10
        digit = digit_sum % 10
        current.next = ListNode(digit)
        current = current.next

    return dummy.next
