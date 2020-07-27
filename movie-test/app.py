from movie import Movie
from user import User

user = User("sarai")

my_movie = Movie("The Matrix", "Sci-fi", True)

user.movies.append(my_movie)

print(user)
print(user.watched_movie())