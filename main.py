from linkedList import LinkedList
from json import load
from quicksort import quicksort
from binary_search import binary_search


categories = ["action", "adventure", "comedy", "drama", "fantasy", "horror", "musical", "parody", "romantic", "sci-fi", "western"]

movies = {}

# initialization of Linked lists

for key in categories:
    movies[key] = LinkedList()

res = []

# loading data from json
j = open("movies.json")
data = load(j)

# sorting the results 
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
    user_input = input("\n\nWich category of movies would you like to look for?\n").lower()
    if user_input == '':
        print("\nEnter a character to search for a category...\n")
        prompt_for_input()
    else:
        target = binary_search(categories, 0, len(categories), user_input)
        if target == "No match found":
            return
        res.append(categories[target])
        if categories[target -1][ :len(user_input)] == categories[target][ :len(user_input)]:
            res.append(categories[target -1])

def prompt_if_no_entries():
    while len(res) == 0:
        list_input = input("\nNo entries for your search...do you wish to see a list of genres available? y/n\n\n").lower()
        while list_input not in ["y", "n"]:
            list_input = input("\nPlease enter y/n\n").lower()
        if list_input == "y":
            string = "|"
            for category in categories:
                print(string + category.capitalize() + string, end=" ")
            prompt_for_input()
        else:
            prompt_for_input()

def choose_category():
    if len(res) < 2:
        user_choice = input(f"\nDo you choose {res[0].capitalize()}? y/n\n").lower()
        while user_choice not in ["y", "n"]:
            user_choice = input("\nPlease enter y/n...\n").lower()
        if user_choice == 'y':
            movies[res[0]].print_movies()
        elif user_choice == 'n':
            res.clear()
    
    else:
        category = input(f"\nThese are the categories available: {res}\n").lower()
        while category not in res:
            category = input(f"\nPlease enter: {' or: '.join([g.capitalize() for g in res])}\n").lower()
        for genre in res:
            if category == genre[ :len(category)]:
                choice = input(f"\nDo you choose {genre.capitalize()}? y/n\n")
                while choice not in ["y", "n"]:
                    choice = input("\nPlease enter y/n...\n").lower()
                if choice == "y":
                    movies[genre].print_movies()
                elif choice == "n":
                    res.clear()


def search_again():
    search = input("\nDo you want to look for another category? y/n\n").lower()
    while search not in ["y", "n"]:
        search = input("\nPlease, enter y/n\n").lower()
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