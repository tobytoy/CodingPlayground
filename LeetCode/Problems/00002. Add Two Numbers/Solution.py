
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode()
        _ = ans
        while (l1 != None) or (l2 != None):
            if l1 == None:
                _.val += l2.val
            elif l2 == None:
                _.val += l1.val
            else:
                _.val += ( l1.val + l2.val )
                
            if (l1!=None):
                l1  = l1.next
            if (l2!=None):
                l2  = l2.next
            
            if _.val > 9:
                _.val -= 10
                _.next = ListNode(1)
            else:
                if (l1 != None) or (l2 != None):
                    _.next = ListNode()
                
            _ = _.next
                
        return ans

if __name__ == '__main__':
    l1_list = [2,4,3]
    l2_list = [5,6,4,5]

    l1 = ListNode(l1_list[0])
    _  = l1 
    for i in l1_list[1:]:
        _.next = ListNode(i)
        _ = _.next
    
    l2 = ListNode(l2_list[0])
    _  = l2 
    for i in l2_list[1:]:
        _.next = ListNode(i)
        _ = _.next

    solution = Solution()
    output = solution.addTwoNumbers(l1, l2)
    print("Output: ")
    _ = output
    while _ != None :
        print(_.val)
        _ = _.next
