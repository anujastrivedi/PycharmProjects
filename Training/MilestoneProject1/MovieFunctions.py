class Movies:
    def __init__(self):
        self.movies_list = []
        self.searched_movie = []

    def add_new_movie(self):
        name = input("Enter the movie name : ")
        director = input("Enter the movie director : ")
        year = input("Enter the movie release year : ")

        self.movies_list.append({"name": name,
                                 "director": director,
                                 "year": year})

    def list_all_movies(self, movie_list):
        if len(movie_list) != 0:
            for movie in movie_list:
                self.list_movie_details(movie)
        else:
            print("No movies found..")

    @classmethod
    def list_movie_details(cls, movie):
        print(f"Name : {movie['name']}")
        print(f"Director : {movie['director']}")
        print(f"Year : {movie['year']}")

    def search_movie(self, movie_list):
        search_by = input("Search movie by : ")
        looking_for = input("What are you looking for? : ")
        self.searched_movie.clear()
        for movie in movie_list:
            for key in movie.keys():
                if key == search_by and movie[key] == looking_for:
                    self.searched_movie.append(movie)
        self.list_all_movies(self.searched_movie)

    def delete_movie(self, movie_list):
        self.search_movie(movie_list)
        if len(self.searched_movie) != 0:
            conf_del = input("R you sure u want to delete this movie? (y/n) : ")
            if conf_del == "y":
                for each in self.searched_movie:
                    movie_list.remove(each)
                print("Deleted Successfully..")
