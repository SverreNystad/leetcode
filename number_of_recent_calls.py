class RecentCounter:

    def __init__(self):
        self.requests = []
        self.time = 3000  # ms

    def ping(self, t: int) -> int:
        self.requests.append(t)

        counter = 0
        range = [t - self.time, t]
        for request in self.requests:
            if range[0] <= request <= range[1]:
                counter += 1
        return counter


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
if __name__ == "__main__":
    obj = RecentCounter()
    count = obj.ping(1)
    assert count == 1
    count = obj.ping(100)
    assert count == 2
    count = obj.ping(3001)
    assert count == 3
    count = obj.ping(3002)
    assert count == 3
