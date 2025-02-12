class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        current = head

        while current and current.next:
            val1 = current
            val2 = current.next

            gdc_value = gcd(val1, val2)
            new_node = ListNode(gdc_value)
            new_node.next = current.next
            current.next = new_node
            current = new_node.next
        return head

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

