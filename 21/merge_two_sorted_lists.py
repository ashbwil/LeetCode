class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        if l1.val <= l2.val:
            head = l1
            head.next = self.mergeTwoLists(l1.next, l2)
        else:
            head = l2
            head.next = self.mergeTwoLists(l1, l2.next)
            
        return head