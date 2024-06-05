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
            if head.get_info():
                for t in head.get_info():
                    print("\n****************************\n")
                    print(f"Title: {t["title"]}")
                    print(f"Director: {t["director"]}")
                    print(f"Rating: {t["rating"]}/10")
                    print(f"Cast: {", ".join(t["cast"])}")
                    print(f"Year: {t["year"]}")
                    print(f"Trama: {t["desc"]}")
            head = head.get_next()