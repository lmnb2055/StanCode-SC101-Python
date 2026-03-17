"""
File: add2.py
Name: Sidney
------------------------
TODO:
"""

import sys


class ListNode:
    def __init__(self, data=0, pointer=None):
        self.val = data
        self.next = pointer


def add_2_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    # 進位數值
    digit_tens = 0
    cur1 = l1
    cur2 = l2
    new_list = None
    # when cur1 and cur2 and digit_tens are None, they should be stopped.
    while cur1 is not None or cur2 is not None or digit_tens != 0:
        if cur1 is not None and cur2 is not None:
            total = cur1.val + cur2.val + digit_tens
        elif cur1 is not None:
            total = cur1.val + digit_tens
        elif cur2 is not None:
            total = cur2.val + digit_tens
        else:
            total = digit_tens
        # calculate the digits
        digit_ones = int(total % 10)
        # calculate the ten digtis
        digit_tens = int(total / 10)

        # 存進去！
        if new_list is None:
            new_list = ListNode(digit_ones, None)
            cur = new_list
        else:
            cur.next = ListNode(digit_ones, None)
            cur = cur.next
        new_list = new_list

        # next cur1,2
        if cur1 is not None:
            cur1 = cur1.next
        if cur2 is not None:
            cur2 = cur2.next

    traversal(new_list)
    return new_list



####### DO NOT EDIT CODE BELOW THIS LINE ########


def traversal(head):
    """
    :param head: ListNode, the first node to a linked list
    -------------------------------------------
    This function prints out the linked list starting with head
    """
    cur = head
    while cur.next is not None:
        print(cur.val, end='->')
        cur = cur.next
    print(cur.val)


def main():
    args = sys.argv[1:]
    if not args:
        print('Error: Please type"python3 add2.py test1"')
    else:
        if args[0] == 'test1':
            l1 = ListNode(2, None)
            l1.next = ListNode(4, None)
            l1.next.next = ListNode(3, None)
            l2 = ListNode(5, None)
            l2.next = ListNode(6, None)
            l2.next.next = ListNode(4, None)
            ans = add_2_numbers(l1, l2)
            print('---------test1---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test2':
            l1 = ListNode(9, None)
            l1.next = ListNode(9, None)
            l1.next.next = ListNode(9, None)
            l1.next.next.next = ListNode(9, None)
            l1.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next.next = ListNode(9, None)
            l2 = ListNode(9, None)
            l2.next = ListNode(9, None)
            l2.next.next = ListNode(9, None)
            l2.next.next.next = ListNode(9, None)
            ans = add_2_numbers(l1, l2)
            print('---------test2---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test3':
            l1 = ListNode(0, None)
            l2 = ListNode(0, None)
            ans = add_2_numbers(l1, l2)
            print('---------test3---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        else:
            print('Error: Please type"python3 add2.py test1"')


if __name__ == '__main__':
    main()
