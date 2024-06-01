class Movie:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def get_title(self):
        return self.value
    
    def get_next(self):
        return self.next
    
    def set_next(self, next_node):
        self.next = next_node