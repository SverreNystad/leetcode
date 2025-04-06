from number_of_recent_calls import RecentCounter


def test_counter():
    obj = RecentCounter()
    count = obj.ping(1)
    assert count == 1
    count = obj.ping(100)
    assert count == 2
    count = obj.ping(3001)
    assert count == 3
    count = obj.ping(3002)
    assert count == 3
