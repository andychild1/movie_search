from movie import Movie

class LinkedList:
    def __init__(self):
        self.head = None

    def add_head(self, value):
        new_movie = Movie(value)
        new_movie.set_next(self.head)
        self.head = new_movie

    def print_movies(self):
        head = self.head
        while head:
            if head.get_title():
                print(head.get_title())
            head = head.get_next()
    

