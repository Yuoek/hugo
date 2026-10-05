from collections import deque

class MovingAverage:
    def __init__(self, size: int):
        self.n = size
        self.s = 0
        self.q = deque()

    def next(self, val: int) -> float:
        if len(self.q) == self.n:
            self.s -= self.q.popleft()
        self.q.append(val)
        self.s += val
        return self.s / len(self.q)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

if __name__ == "__main__":
    ma = MovingAverage(3)
    print(ma.next(1))   # 1.0
    print(ma.next(10))  # (1+10)/2 = 5.5
    print(ma.next(3))   # (1+10+3)/3 ≈4.666666666666667
    print(ma.next(5))   # (10+3+5)/3 =6.0
