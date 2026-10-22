class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val 
        # next and prev
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        # init a cache, and left right node
        self.cache = {} # key is key, val is node 
        # init capacity
        self.cap = capacity
        # need a left and right node
        self.right = Node(0, 0)
        self.left = Node(0, 0)
        # link them to each other 
        self.right.prev = self.left 
        self.left.next = self.right 
    
    # create helper REMOVE and insert helper 
    # remove ONLY removes it from LL, not cache.
    def remove(self, node): # POINTER FUNCTION, you're just moving LL pointers.
        # this will remove the node we need to remove
        prevNode = node.prev
        nextNode = node.next 

        prevNode.next = nextNode # move prev's next OVER removed Node
        nextNode.prev = prevNode # move next's prev BACK OVER removed Node

    
    def insert(self, node):
        # this will insert linked list and update MRU, by INSERTING NODE AT RIGHT-most position 
        # places node at MRU position, BEHIND our right pointer.
        prevNode = self.right.prev 
        nextNode = self.right

        # now point those both to node so it's in the middle 
        nextNode.prev = node 
        prevNode.next = node

        # establish node's 
        node.prev = prevNode
        node.next = nextNode



    def get(self, key: int) -> int:
        if key in self.cache: # after GETTING, we want to remove from list, then re-insert 
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1 

    def put(self, key: int, value: int) -> None:
        # if we have key already in our cache, we want to update it in our cache
        if key in self.cache:
            # remove from LL
            self.remove(self.cache[key])
            #del self.cache[key] guess maybe we do this in the remove func?
        # then update both cache and LL
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # check cap
        if len(self.cache) > self.cap:
            # remove LRU from LL, del from cache. 
            # self.left.next ALWAYS going to be LRU, so remove it
            lru = self.left.next 
            # delete from LL
            self.remove(lru)
            # del from cache
            del self.cache[lru.key] # STILL have key, because it's inside the NODE itself, which is still saved in var

