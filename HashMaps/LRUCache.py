class CacheNode:
    def __init__(self, previous =None, next=None, key=None):
        self.previous = previous
        self.next = next
        self.key = key
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # val:
        self.cacheStack = CacheNode()
        self.cacheKeys = []
        self.cacheFreeCapacity = capacity
    def get(self, key: int) -> int:
        if(self.cache.get()):
            # remove from stack 
            # move to top of stack
            # return val
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if(self.cache.get(key)):
            self.cache[key] = value
        else:
            if(self.cacheFreeCapacity > 0):
                self.cache[key] = value
            else:
                # remove LRU
                # add new
                self.cache[key] = value

    def removeFromStack(self, key):
        dummy = self.cacheStack
        while(dummy):
            if(dummy.key == key):
                prev = dummy.previous
                prev.next = dummy.next


if __name__ == "__main__":
    testcase1 = ""
    expected1 = ""
    testcase2 = ""
    expected2 = ""
    testcase3 = ""
    expected3 = ""
    solution = LRUCache()
    solution.function(testcase1)