

from odd_even_linked_list import ListNode, Solution


def test_reverse_incrementing_list():

    node_5 = ListNode(5)
    node_4 = ListNode(4, node_5)
    node_3 = ListNode(3, node_4)
    node_2 = ListNode(2, node_3)
    node_1 = ListNode(1, node_2)
    
    reversed_order = [node_1,
                      node_2,
                      node_3,
                      node_4,
                      node_5,
                      ]

    result = Solution().oddEvenList(node_1)
