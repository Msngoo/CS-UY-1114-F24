class MyFloatPair:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
    def __str__(self):
        return f"The first value: {self.first} and second value: {self.second}"
    
    def get_first(self):
        return self.first
    def set_first(self, new_first):
        self.first = new_first
    def get_second(self):
        return self.second
    def set_first(self, new_second):
        self.first = new_second
    def __add__(self, other):
        new_fp = MyFloatPair(self.first + other.first, self.second + other.second)
        return new_fp
    def __lt__(self, other):
        lessThan = (self.first < other.first and self.second < other.second)
        return lessThan
def main():
    pair1 = MyFloatPair(1.0, 2.0)
    pair2 = MyFloatPair(3.0, 4.0)
    pair3 = MyFloatPair(5.0, 6.0)
    pair4 = MyFloatPair(7.0, 8.0)
    pair5 = MyFloatPair(9.0, 10.0)
    pairList = [pair1, pair2, pair3, pair4, pair5]
    for pair in pairList:
        print(pair)

    newPair = pair1 + pair2 #new float pair is created as a result; auto calls pair1.__add__(pair2)
    print(newPair)
    print(pair1 < pair2)
main()

        