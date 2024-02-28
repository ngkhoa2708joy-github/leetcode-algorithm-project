# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        elif list1 == None and list2 == None:
            return None
        else:
            current = dummy = ListNode(-1)
            while (list1 != None and list2 != None):
                if list1.val < list2.val:
                    current.next = list1    
                    list1 = list1.next
                    current = current.next
                else:
                    current.next = list2
                    list2 = list2.next
                    current = current.next
            
            if list1 == None:
                current.next = list2
            if list2 == None:
                current.next = list1
        return dummy.next

if __name__ == "__main__":
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)
    
    list2 = ListNode(1)
    list2.next = ListNode(2)
    list2.next.next = ListNode(7)
    list2.next.next.next = ListNode(8)
    
    solution = Solution()
    merge_list = solution.mergeTwoLists(list1, list2)
    
    while(merge_list != None):
        print(merge_list.val, end = " -> ")
        merge_list = merge_list.next
    print("None")
    