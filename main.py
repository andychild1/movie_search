# movie recommendation software
# binary search as algorithm
# data structure for storing movies categories
# action, adventure, comedy, drama, fantasy, horror, musical, parody, sci-fi, western

from linked_list import LinkedList
from json import load
from quicksort import quicksort


categories = ["action", "adventure", "comedy", "drama", "fantasy", "horror", "musical", "parody", "sci-fi", "western"]

movies = {}

# initialization of Linked lists

for key in categories:
    movies[key] = LinkedList()

res = []


j = open("movies.json")
data = load(j)

for key, value in movies.items():
    val = [v for v in data[key]]
    start = 0
    end = len(val) - 1
    quicksort(val, start, end)
    value.add_head(val)

print(r'''\

  __  __            _        _____ _           _           
 |  \/  | _____   _(_) ___  |  ___(_)_ __   __| | ___ _ __ 
 | |\/| |/ _ \ \ / / |/ _ \ | |_  | | '_ \ / _` |/ _ \ '__|
 | |  | | (_) \ V /| |  __/ |  _| | | | | | (_| |  __/ |   
 |_|  |_|\___/ \_/ |_|\___| |_|   |_|_| |_|\__,_|\___|_|   
                                                           
''')

def prompt_for_input():
    user_input = input("\nWich category of movies would you like to look for?\n")
    if user_input == '':
        print("\nEnter a character to search for a category...\n")
        prompt_for_input()
    else:
        for category in categories:
            if user_input == category[ :len(user_input)]:
                res.append(category)

def prompt_if_no_entries():
    while len(res) == 0:
        print("\nNo entries for your search...try again\n")
        prompt_for_input()

def choose_category():
    if len(res) < 2:
        user_choice = input(f"\nDo you choose {res[0].capitalize()}? y/n\n")
        while user_choice not in ["y", "n"]:
            user_choice = input("\nPlease enter y/n...\n")
        if user_choice == 'y':
            movies[res[0]].print_movies()
        elif user_choice == 'n':
            res.clear()
    
    else:
        category = input(f"\nThese are the categories available: {res}\n")
        while category not in res:
            category = input(f"\nChoose between: {" | ".join(res)}\n")
        for genre in res:
            if category == genre[ :len(category)]:
                choice = input(f"\nDo you choose {genre.capitalize()}? y/n\n")
                while choice not in ["y", "n"]:
                    choice = input("\nPlease enter y/n...\n")
                if choice == "y":
                    movies[genre].print_movies()
                elif choice == "n":
                    res.clear()


def search_again():
    search = input("\nDo you want to look for another category? y/n\n")
    while search not in ["y", "n"]:
        search = input("\nPlease, enter y/n\n")
    if search == "y":
        res.clear()
        prompt_for_input()
        prompt_if_no_entries()
        choose_category()
        search_again()
    else:
        print("+++++++++++++++++++++++++++++++++++")
        print("\nThank you for using Movie Finder!\n")
        print("+++++++++++++++++++++++++++++++++++")
        return

    


print("\nWelcome to 'Movie Finder!'\n")


prompt_for_input()
prompt_if_no_entries()
choose_category()
search_again()


