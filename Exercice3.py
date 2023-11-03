class Exercice3:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity
 
    def get(self, key: int):
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]
 
    def put(self, key, value):
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last = False)

    def free(self):
        # Implémenter la logique de libération
        pass
    
    