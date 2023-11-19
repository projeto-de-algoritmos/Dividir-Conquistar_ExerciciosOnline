class ListNode(object):
    def __init__(self, val=0, next=None):
       self.val = val
       self.next = next

class Solution:
    class Solution:
        def mergeKLists(self, lists):
            if not lists or len(lists) == 0:
                return None
            
            while len(lists) > 1:
                merged_lists = []

                for i in range(0, len(lists), 2):
                    l1 = lists[i]
                    l2 = lists[i + 1] if (i + 1) < len(lists) else None
                    merged_lists.append(self.mergeTwoLists(l1, l2))
                lists = merged_lists
            
            return lists[0]
        
        def mergeTwoLists(self, l1, l2):
            aux = ListNode()
            tail = aux
            
            while l1 and l2:
                if l1.val < l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next   
                tail = tail.next           
            if l1:
                tail.next = l1
            elif l2:
                tail.next = l2            
            return aux.next