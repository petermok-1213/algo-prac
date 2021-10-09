from math import e, inf

class PriorityQueue():

    def __init__(self) -> None:
        self.queue = {}     # [ (key0, weight0), (key1, weight1), ...]

    # return if the list is empty, O(1) time
    def is_empty(self):
        return len(self.queue) == 0

    # insert key, weight into the list, O(1) time
    def insert(self, key: int, weight: int) -> None:
        self.queue[key] = weight

    # modify the weight at the key, raise exception if key not found
    def update(self, key: int, weight: int) -> None:
        if key in self.queue:
            self.queue[key] = weight
        else:
            raise KeyError("Key not found")

    # pop the key with the least weight, return -1 if the list is empty
    # O(n) time
    def pop(self) -> int:
        if not self.is_empty():
            min_weight = inf
            min_key = None
            for key, weight in self.queue.items():        
                if min_weight > weight:   
                    min_key = key
                    min_weight = weight      
            self.queue.pop(min_key)
            return min_key
        else:
            return -1


if __name__ == "__main__":
    
    q = PriorityQueue()
    q.insert(1, 10)
    q.insert(2, 5)
    print(q.pop() == 2)
    q.update(1, 4)
    print(q.queue[1]==4)
    q.update(2, 10)
