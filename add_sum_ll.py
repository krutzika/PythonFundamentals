
class LinkedList:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class AddNumbers:

    def add_numbers(self, l1, l2):
        dummy = LinkedList(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1+val2 + carry
            carry = total//10
            digit = total % 10
            current.next = LinkedList(digit)
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

def main():
    add_number = AddNumbers()
    l1 = LinkedList(2, LinkedList(4, LinkedList(3)))  # Represents 342
    l2 = LinkedList(5, LinkedList(6, LinkedList(4)))
    solutions = add_number.add_numbers(l1, l2)
    print(solutions)