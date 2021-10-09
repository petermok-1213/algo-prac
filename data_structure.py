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

    # modify the weight at the key, raise exception if key not found
    def update(self, key: int, weight: int) -> None:
        for i in range(len(self.queue)):
            if self.queue[i][0] == key:
                self.queue[i] = (key, weight)
            return
        raise KeyError("Key not found in queue")   # somehow this doesnt work?


if __name__ == "__main__":

    # testing the insert and pop method
    Q = PriorityQueue()
    Q.insert(1, 10)
    Q.insert(2, 5)

    print(Q.pop() == 2)
    print(Q.pop() == 1)
    print(Q.pop() == -1)

    # testing the update method
    Q = PriorityQueue()
    Q.insert(5, 10)
    Q.update(5, 8)
    print(Q.queue[0][1] == 8)
    print(Q.update(6, 10))
    print(Q.queue[0][1])
