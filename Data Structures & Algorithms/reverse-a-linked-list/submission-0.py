# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ll=[]
        curr=head
    
        while curr != None:
            ll.append(curr.val)
            curr = curr.next

        curr = head    

        # reverse the list 

        first = 0
        last = len(ll)-1

        while first < last:
            temp = ll[first]
            ll[first]=ll[last]
            ll[last]=temp

            first+=1
            last-=1
        
        for i in ll:
            curr.val=i
            curr = curr.next

        return head    

        
        
              



        

        

        