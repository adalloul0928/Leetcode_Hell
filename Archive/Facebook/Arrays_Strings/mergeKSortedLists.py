# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists) -> ListNode:
        N = len(lists)
        if N == 0:
            return None
        elif N == 1:
            return lists[0]
        elif N == 2:
            head = pointer = ListNode(0)
            l1 = lists[0]
            l2 = lists[1]
            while l1 and l2:
                if l1.val <= l2.val:
                    pointer.next = l1
                    l1 = l1.next
                else:
                    pointer.next = l2
                    l2 = l2.next
                pointer = pointer.next
            if l1:
                pointer.next = l1
            elif l2:
                pointer.next = l2
            return head.next

        mid = N//2
        leftList = self.mergeKLists(lists[:mid])
        rightList = self.mergeKLists(lists[mid:])
        return self.mergeKLists(leftList, rightList)

    # flipping approach although this is O(n*logn)
    def mergeKLists3(self, lists):
        result = []
        for list in lists:
            if list == None:
                continue
            while list != None:
                result.append(list.val)
                list = list.next

        result.sort()
        result.reverse()

        priorNode = None

        for num in result:
            node = ListNode(num)
            node.next = priorNode
            priorNode = node
        return priorNode

    # mergesort take 2
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        N = len(lists)
        if N == 0:
            return None

        if N == 1:
            return lists[0]

        if N == 2:
            head = ListNode(0)
            cur = head
            l1 = lists[0]
            l2 = lists[1]
            while l1 and l2:
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next

                cur = cur.next

            if l1:
                cur.next = l1
            if l2:
                cur.next = l2

            return head.next

        mid = N // 2
        l1 = self.mergeKLists(lists[0:mid + 1])
        l2 = self.mergeKLists(lists[mid + 1:])

        return self.mergeKLists([l1, l2])

    # mergeSort approach
    def mergeKLists(self, lists):
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else lists

    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l2.next
            point = point.next
        if not l1:
            point.next = l2
        else:
            point.next = l1
        return head.next

    # Nk approach where we merge two lists k times (where k is the number of lists)
    def mergeKLists2(self, lists) -> ListNode:
        def merge2lists(l1, l2):
            if not new_list:
                return l2
            if not l2:
                return l1
            if l1.val > l2.val:
                l1.next = merge2lists(l1.next, l2)
                return l1
            else:
                l2.next = merge2lists(l1, l2.next)
                return l2

        if not list[0]:
            return None

        new_list = lists[0]
        for ind in range(1, len(lists)):
            new_list = merge2lists(new_list, lists[ind])
        return new_list