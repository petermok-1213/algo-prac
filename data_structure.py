from math import inf

class PriorityQueue():

    def __init__(self) -> None:
        self.queue = []     # [ (key0, weight0), (key1, weight1), ...]

    # return if the list is empty, O(1) time
    def is_empty(self):
        return len(self.queue) == 0

    # insert key, weight into the list, O(1) time
    def insert(self, key: int, weight: int) -> None:
        self.queue.append((key, weight))

    # pop the key with the least weight, return -1 if the list is empty
    # O(n) time
    def pop(self) -> int:
        if not self.is_empty():
            min_weight = inf
            min_key = None
            for tup in self.queue:  # tup[0] -> key, tup[1] -> weight
                if min_weight > tup[1]:
                    min_key = tup[0]
                    min_weight = tup[1]
            self.queue.remove((min_key, min_weight))
            return min_key
        else:
            return -1

if __name__ == "__main__":

    Q = PriorityQueue()
    Q.insert(1, 10)
    Q.insert(2, 5)

    print(Q.pop() == 2)
    print(Q.pop() == 1)
    print(Q.pop() == -1)