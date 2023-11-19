class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution():
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        l = head
        r = self.getMeio(head)
        temp = r.next 
        r.next = None
        r = temp

        l = self.sortList(l)
        r = self.sortList(r)

        return self.merge(l, r)
    
    def getMeio(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def merge(self, list1, list2):
        aux = tail = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1 != None:
            tail.next = list1
        if list2 != None:
            tail.next = list2

        return aux.next


# TESTES 

def printList(node):
    while node:
        print(node.val, end=" ")
        node = node.next
    print()

head = ListNode(3)
head.next = ListNode(1)
head.next.next = ListNode(4)
head.next.next.next = ListNode(2)

sol = Solution()

sorted_list = sol.sortList(head)

print("Lista encadeada ordenada:")
printList(sorted_list)