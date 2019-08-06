from str2bool import str2bool


class Books:
    def __init__(self):
        self.books_list = []
        self.searched_book_list = []

    def add_new_book(self):
        name = input("Enter the book name : ")
        author = input("Enter the book author : ")
        while True:
            read = input("Set the read flag for the book to \'true/false\' : ").lower()
            if read == "true" or read == "false":
                read = str2bool(read)
                break
            else:
                print("Invalid input..")

        self.books_list.append({"name": name,
                                "author": author,
                                "read": read})

    def list_all_books(self, books_list):
        if len(books_list) != 0:
            for book in books_list:
                self.list_book_details(book)
        else:
            print("Books not found..")

    @staticmethod
    def list_book_details(book):
        print(f"Name : {book['name']}")
        print(f"Author : {book['author']}")
        print(f"Read : {book['read']}")

    def search_book(self):
        search_by = input("Search book by : ")
        looking_for = input("What are you looking for? : ")

        if looking_for.lower() == "true" or looking_for.lower() == "false":
            looking_for = str2bool(looking_for)

        self.searched_book_list.clear()
        self.searched_book_list = self.search_book_by_attribute(search_by, looking_for, self.books_list)
        if self.searched_book_list:
            self.list_all_books(self.searched_book_list)
        else:
            print("Books not Found..")

    @staticmethod
    def search_book_by_attribute(search_by, looking_for, book_list):
        try:
            filter_obj = filter(lambda x: x[search_by] == looking_for, book_list)
            searched_book_list = list(filter_obj)
        except KeyError:
            print("Search key not found.. Try again..")
            searched_book_list = []
        return searched_book_list

    def delete_book(self):
        self.search_book()

        if len(self.searched_book_list) != 0:
            conf_del = input("R you sure u want to delete this Book? (y/n) : ")
            if conf_del == "y":
                for each in self.searched_book_list:
                    self.books_list.remove(each)
                print("Deleted Successfully..")

    def update_book_detail(self):
        search_by = "name"
        looking_for = input("Enter a book name u want to edit : ")

        self.searched_book_list.clear()
        self.searched_book_list = self.search_book_by_attribute(search_by, looking_for, self.books_list)

        if len(self.searched_book_list) != 0:
            self.list_all_books(self.searched_book_list)

            conf_update = input("R you sure u want to toggle the read flag of this Book? (y/n) : ")
            if conf_update == "y":
                for each in self.searched_book_list:
                    each['read'] = not each['read']
                print("Updated Successfully..")
        else:
            print("Books not Found..")
