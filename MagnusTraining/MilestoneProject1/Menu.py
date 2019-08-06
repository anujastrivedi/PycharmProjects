# from MilestoneProject1.MovieFunctions import Movies
from MilestoneProject1.MovieFunctionsWithFile import Movies


def menu():
    movie = Movies()
    while True:
        menu_selection = input(
            "Enter \'a\' to add a movie, \'l\' to list all movies, \'s\' to search a movie, "
            "\'d\' to delete a movie and \'q\' to quit : ")

        if menu_selection == 'q':
            break
        elif menu_selection == 'a':
            movie.add_new_movie()
        elif menu_selection == 'l':
            movie.read_file()
            movie.list_all_movies(movie.movies_list)
        elif menu_selection == 's':
            movie.read_file()
            movie.search_movie(movie.movies_list)
        elif menu_selection == 'd':
            movie.read_file()
            movie.delete_movie(movie.movies_list)
        else:
            print("Unknown command..")



menu()
