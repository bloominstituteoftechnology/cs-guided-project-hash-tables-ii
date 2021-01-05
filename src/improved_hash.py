"""
Here's our improved hash table implementation that uses linked list chaining to handle collisions:

Your task is create your own HashTable without using a built-in library.
​
Your HashTable needs to have the following functions:
​
- put(key, value) : Inserts a (key, value) pair into the HashTable. If the
value already exists in the HashTable, update the value.
- get(key): Returns the value to which the specified key is mapped, or -1 if
this map contains no mapping for the key.
- remove(key) : Remove the mapping for the value key if this map contains the
mapping for the key.
​
Example:
​
```plaintext
hash_table = MyHashTable();
hash_table.put("a", 1);
hash_table.put("b", 2);
hash_table.get("a");            // returns 1
hash_table.get("c");            // returns -1 (not found)
hash_table.put("b", 1);         // update the existing value
hash_table.get("b");            // returns 1
hash_table.remove("b");         // remove the mapping for 2
hash_table.get("b");            // returns -1 (not found)
```
"""
# O(1)
def hash_fn(key, length):
    return id(key) % length
​
# Linked list so that we can implement linked list chaining 
class ListNode:
    def __init__(self, key, value):
        self.key = key 
        self.value = value 
        self.next = None
​
class MyHashTable:
    def __init__(self, capacity, hash_fn=hash_fn):
        # Your code here
        # init our storage with some positive number of empty slots 
        self.storage = [None] * capacity
        # Some function that takes a key and spits out an integer 
        # we can make sure that the output is in bounds of our storage
        # by using % 
        self.hash_fn = hash_fn
​
    def print_storage(self):
        print(self.storage)
​
    '''
    Add the key and value as a pair in the hash table. 
    If the value already exists in the HashTable, update the value.
    '''
    def put(self, key, value):
        # Your code here
        # 1. Run the key through our hash function 
        # 2. set storage[index] = (key, value)
        # This will have the effect of updating a key that already existed 
        # in our hash table 
        # Doesn't handle collisions at all 
        index = self.hash_fn(key, len(self.storage))
​
        # check if this index is taken 
            # if it is taken, check the incoming key against the current key 
            # if they match, overwrite 
            # if they don't, still overwrite, but also print a message saying
            # we're overwriting 
        if self.storage[index] is not None:
            # we are inserting a key that already exists 
            # we want to overwrite the key's value 
            # but it isn't enough to just check the first linked list node 
            # at this index; we need to traverse the linked list
            current = self.storage[index]
​
            while current is not None:
                if current.key != key:
                    current = current.next
                else:
                    # we found the key whose value we want to overwrite 
                    current.value = value
                    break
​
                if current.next is None:
                    # if we reach the end of the while loop, then we didn't end up
                    # overwriting a value; instead we need to add a new node to
                    # the end of the linked list 
                    current.next = ListNode(key, value)
        else:
            self.storage[index] = ListNode(key, value)
​
    '''
    Return the value associated with the given key.
    If the key doesn't exist in the hash table, should return -1
    '''
    def get(self, key):
        # Your code here
        # 1. Run our hash function on our key 
        # 2. Check to see if the index is empty or not 
        #   - if it is, return -1 
        #   - otherwise, return the value 
        index = self.hash_fn(key, len(self.storage))
​
        if self.storage[index] is None:
            return -1
​
        # otherwise, there's a linked list at this index
        # iterate through it to try and find the specified key 
        current = self.storage[index] 
​
        while current is not None:
            if current.key == key:
                return current.value
            
            current = current.next 
​
        # we reached the end of the linked list and none of the 
        # keys matched what we were looking for 
        return -1
​
    '''
    Removes the key-value pair specified by the key.
    Set the spot where the key-value pair is to None.
    Doesn't return anything.
    '''
    def remove(self, key) -> None:
        # Your code here
        # 1. Run our hash function on our key 
        # 2. Set self.storage[index] = None
        index = self.hash_fn(key, len(self.storage))
​
        if self.storage[index] is not None:
            # we need to keep track of both the current node as well 
            # as the previous node 
            # when the current node's key is the one we're looking for 
            # set the previous node's next to refer to current's next 
            # don't forget to check the first node in the linked list 
            if self.storage[index].key == key:
                # remove the first linked list node 
                self.storage[index] = self.storage[index].next
                return 
​
            prev = self.storage[index]
            current = prev.next
​
            while current is not None:
                if current.key == key:
                    prev.next = current.next
                    break
​
                prev = current 
                current = current.next
​
hash_table = MyHashTable(10)
# ht.put('cat', 'dog')
# ht.print_storage()
# ht.put('cat', 'tiger')
# ht.print_storage()
​
hash_table.put("a", 1)
hash_table.put("b", 2)
print(hash_table.get("a"))
print(hash_table.get("c"))
hash_table.put("b", 1)         
print(hash_table.get("b"))
hash_table.remove("b")         
print(hash_table.get("b"))