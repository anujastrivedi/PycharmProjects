from MilestoneProject2.DatabaseConnection import DBConnect
from str2bool import str2bool


class Books:

    @classmethod
    def add_new_book(cls):
        name = input("Enter the book name : ")
        author = input("Enter the book author : ")
        while True:
            read = input("Set the read flag for the book to \'true/false\' : ").lower()
            if read == "true" or read == "false":
                read = str2bool(read)
                break
            else:
                print("Invalid input..")

        books_list = [(name, author, read)]

        dbconnect = DBConnect()
        dbconnect.insert_value(books_list)

    @classmethod
    def list_all_books(cls, books_list):
        if len(books_list) != 0:
            for book in books_list:
                Books.list_book_details(book)
        else:
            print("Books not found..")

    @staticmethod
    def list_book_details(book):
        print(f"Name : {book[1]}")
        print(f"Author : {book[2]}")
        print(f"Read : {bool(book[3])}")

    @classmethod
    def search_book(cls):
        search_by = input("Search book by : ").lower()
        looking_for = input("What are you looking for? : ")

        searched_book_list = []
        if search_by == "name" or search_by == "author" or search_by == "read":
            if looking_for.lower() == "true" or looking_for.lower() == "false":
                looking_for = str2bool(looking_for)

            dbconnect = DBConnect()
            searched_book_list = (dbconnect.search_value(search_by, looking_for)).copy()

            if searched_book_list:
                cls.list_all_books(searched_book_list)
            else:
                print("Books not Found..")
        else:
            print("Invalid Search key.. Try again..")
        return searched_book_list

    @classmethod
    def delete_book(cls):
        searched_book_list = cls.search_book()

        if len(searched_book_list) != 0:
            conf_del = input("R you sure u want to delete this Book? (y/n) : ")
            if conf_del == "y":
                dbconnect = DBConnect()
                dbconnect.delete_value(searched_book_list)
                print("Deleted Successfully..")

    @classmethod
    def update_book_detail(cls):
        search_by = "name"
        looking_for = input("Enter a book name u want to edit : ")

        dbconnect = DBConnect()
        searched_book_list = dbconnect.search_value(search_by, looking_for)

        if len(searched_book_list) != 0:
            cls.list_all_books(searched_book_list)

            conf_update = input("R you sure u want to toggle the read flag of this Book? (y/n) : ")
            if conf_update == "y":
                updated_searched_book_list = []
                for each in searched_book_list:
                    each_list = list(each)
                    each_list[3] = not each_list[3]
                    updated_searched_book_list.append(tuple(each_list))

                dbconnect.update_value(updated_searched_book_list)
                print("Updated Successfully..")
        else:
            print("Books not Found..")
