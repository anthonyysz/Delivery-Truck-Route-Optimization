
#This HashTable class uses code from WGU's "C950 Webinar-2 - Getting Greedy, who moved my data?". Cited in Section I of write-up.

class HashTable:
    def __init__(self):
        self.capacity = 40 #There will be 40 packages
        self.list = [] 
        for i in range(self.capacity): 
            self.list.append([])
            
    def insert(self, key, package): #Insert function taken from source 1
        bucket = hash(key) % len(self.list)
        bucket_list = self.list[bucket]
        
        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = package
                return True
            
        key_value = [key, package]
        bucket_list.append(key_value)
        return True
            
    def lookup(self, key): #This lookup will return basic details about the package
        bucket = hash(key) % len(self.list)
        bucket_list = self.list[bucket] #Getting the bucket list
        
        for kv in bucket_list: #Finding the correct key and returning the necessary details for this function
            if kv[0] == key:
                return [kv[1].idnum, kv[1].address, kv[1].deadline, kv[1].city, kv[1].zipcode, 
                        kv[1].weight, kv[1].status]
            
    def return_package(self, key): #Using the same base function as previous, except this time returning the package item
        bucket = hash(key) % len(self.list)
        bucket_list = self.list[bucket]
        
        for kv in bucket_list:
            if kv[0] == key:
                return kv[1]