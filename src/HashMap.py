class HashMap():
    hashtable:dict[str:object]

    def __init__(self):
        self.hashtable = {}
    def add(self,key:str,value:object):
        self.hashtable[key] = value
    def get(self,key:str):
        return self.hashtable[key]
    def remove(self,key:str):
        del self.hashtable[key]
    def update(self,key:str,value:object):
        self.hashtable[key] = value
    def clear(self):
        self.hashtable.clear()
    def contains(self,key:str):
        return key in self.hashtable
    @property
    def size(self):
        return len(self.hashtable)
    @property
    def keys(self):
        return self.hashtable.keys()
        
