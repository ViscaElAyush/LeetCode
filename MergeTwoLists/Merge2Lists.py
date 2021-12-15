# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1   
        
        if list1.val <= list2.val:
            head = ListNode(list1.val)
            list1 = list1.next
        else:
            head = ListNode(list2.val)
            list2 = list2.next
       
        new = head
        
        while True:
            if list1 == None:
                new.next = list2
                return head
            elif list2 == None:
                new.next = list1
                return head
            elif list1 == None and list2 == None:
                return head
            
            if list1.val <= list2.val:
                new.next = ListNode(list1.val)
                list1 = list1.next
                new = new.next
            else:    
                new.next = ListNode(list2.val)
                list2 = list2.next
                new = new.next