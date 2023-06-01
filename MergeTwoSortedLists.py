# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        t1,t2=l1,l2
        head=ListNode()
        temp=head

        while t1 is not None and t2 is not None:
            if t1.val<t2.val:
                curr=ListNode(t1.val)
                temp.next=curr
                temp=temp.next
                t1=t1.next
            else:
                curr=ListNode(t2.val)
                temp.next=curr
                temp=temp.next
                t2=t2.next

        while t1 is not None:

            curr=ListNode(t1.val)
            temp.next=curr
            temp=temp.next
            t1=t1.next

        while t2 is not None:

            curr=ListNode(t2.val)
            temp.next=curr
            temp=temp.next
            t2=t2.next


        return head.next

        

            

        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """