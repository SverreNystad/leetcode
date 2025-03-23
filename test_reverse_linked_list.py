from reverse_linked_list import Solution, ListNode


def test_reverse_empty_list():


    result = Solution().reverseList(None)
    assert result == None


def test_reverse_single_list():

    node_1 = ListNode()

    result = Solution().reverseList(node_1)
    assert result == node_1

