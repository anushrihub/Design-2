# https://leetcode.com/problems/design-hashmap/

# we are handling dummy -1, -1 for every used bucket. because while remove ooperation link could discrupt so dummy will be constant

# self.storage is your array of buckets. Each bucket is a linked list.

# index = self.get_hash(key) tells us which bucket the key belongs to.

# So self.storage[index] is the head of the linked list for that bucket.

# creating a class MyHashMap
class MyHashMap:
    # need storage to add the key, value pairs. Intialising the storage 
    def __init__(self):
        self.bucket = 1000
        self.storage = [None] * self.bucket

    class Nodes:
        # initialing the attribute of Nodes class. This hashmap acts like a linked list so every node has to store a pointer of a next node. Hence this class has three attributes key, value and next. when there is a single node we dont know it's next hence it's default value is None
        def __init__(self, key, value):
                self.key = key
                self.value = value
                self.next = None 
        
    # need to find a bucket in a map to store the key and value. it return the bucket
    def get_hash(self, key) -> int:
        return key % self.bucket 

    # method to get the prev pointer in the linked list. we are using linked list so if we have to remove middle node we need to connect previous to the next or to add need to connect previous to the newly added and newly added to the next hence this method is useful
    def get_prev(self, head, key):
        prev = None
        curr = head
        # we need to find the prev pointer of the given key so we are looping until we find the key hence we are providing two conditions curr is not None and curr key is not equal to provided key
        while curr is not None and curr.key != key:
            prev = curr
            curr = curr.next
        # when we find the matching key exit the loop and make current pointer as previous so that we can perform put and remove function
        return prev
        
    # method to insert the key and value pair
    def put(self, key: int, value: int) -> None:
        # we are finding the location where the key is stored to do this we call the previously defined method and stored into the variable so that we can use that variable to insert the key
        index = self.get_hash(key)
        # self.storage[index] is the head of the bucket. if there is nothing in this bucket means no head
        if self.storage[index] is None:
            # denoting first element is (-1,-1) in hashmap
            self.storage[index] = self.Nodes(-1, -1)
            # we then attach the key and value which we are providing the next of that dummy node
            self.storage[index].next = self.Nodes(key, value)
            # We’re saying: “We just created the linked list for this bucket and inserted the first node. No further work is needed, so exit the function
            return
        # if the bucket is not empty we call the prev method to find the previous pointer of the current key, value.
        prev = self.get_prev(self.storage[index], key)
        # if the next of the previous is none we can directly add key value pair that is node because there is no node at next
        if prev.next is None:
            prev.next = self.Nodes(key, value)
        # but if there is next node then we need to update the existing value with the new value and key remain unchanged
        else:
            prev.next.value = value

    # method to return the value of the key
    def get(self, key: int) -> int:
        # we are finding the location(bucket) where the key is stored to do this we call the previously defined method and stored into the variable so that we can use that variable to insert the key
        index = self.get_hash(key)
        # self.storage[index] is the head of the bucket. if no keys have been inserted into this bucket yet, it’s empty means no head
        if self.storage[index] is None:
            return -1
        # call the prev method to find the previous pointer of the current key, value. and at this time self.storage[index] is (-1, -1) beacuse we added this in the put function
        prev = self.get_prev(self.storage[index], key)
        # if the prev is the last node then there nothing at next so return -1
        if prev.next is None:
            return -1
        # If prev.next is not None, it points to the node containing the key.
        return prev.next.value       
            
    # method to remove the key and it's correspondent element
    def remove(self, key: int) -> None:
        # find the bucket
        index= self.get_hash(key)
        # if there is no head bucket is empty 
        if self.storage[index] is None:
            return -1
        # if there is something in the bucket call the prev method to find the previous pointer of the current key, value. and at this time self.storage[index] is (-1, -1) beacuse we added this in the put functions
        prev = self.get_prev(self.storage[index], key)
        if prev.next is None:
            return -1
        # link the next node of previous with the next to next node
        prev.next = prev.next.next
            

# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(2,200)
print(obj.put(2,200))
param_2 = obj.get(2)
obj.remove(2)