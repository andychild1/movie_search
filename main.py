# movie recommendation software
# binary search as algorithm
# data structure for storing movies categories
# action, adventure, comedy, drama, fantasy, horror, musical, parody, sci-fi, western

from linked_list import LinkedList
from json import load
from quicksort import quicksort


movies = ["action", "adventure", "comedy", "drama", "fantasy", "horror", "musical", "parody", "sci-fi", "western" ]
'''
res = []
user_input = input("Wich movie category do you want to search for? Type the beginnig of that movie category...")
for movie in movies:
    if user_input == movie[:len(user_input)]:
        res.append(movie)
    
print("Theese are the results available: ", res)

'''
j = open("movies.json")
data = load(j)


act = [d for d in data["action"]]

# quicksort initialization
start = 0
end = len(act) - 1
quicksort(act, start, end)

action = LinkedList()
action.add_head(act)
action.print_movies()