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
                    print("Title: {}".format(t["title"]))
                    print("Director: {}".format(t["director"]))
                    print("Rating: {}/10".format(t["rating"]))
                    print("Cast: {}".format(",".join(t["cast"])))
                    print("Year: {}".format(t["year"]))
                    print("Trama: {}".format(t["desc"]))
            head = head.get_next()