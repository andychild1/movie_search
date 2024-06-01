# movie recommendation software
# binary search as algorithm
# data structure for storing movies categories
# action, adventure, comedy, drama, fantasy, horror, musical, parody, sci-fi, western

movies = ["action", "adventure", "comedy", "drama", "fantasy", "horror", "musical", "parody", "sci-fi", "western" ]

res = []
user_input = input("Wich movie category do you want to search for? Type the beginnig of that movie category...")
for movie in movies:
    if user_input == movie[:len(user_input)]:
        res.append(movie)
    
print("Theese are the results available: ", res)