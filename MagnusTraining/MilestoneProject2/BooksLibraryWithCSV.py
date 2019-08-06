import csv
import os.path
from str2bool import str2bool


class Books:

    filename = "books_list.csv"

    @staticmethod
    def write_file(books_list):
        with open(Books.filename, 'w', newline='') as fp:
            if len(books_list) != 0:
                wr = csv.DictWriter(fp, books_list[0].keys())
                wr.writeheader()
            else:
                wr = csv.writer(fp)
            for each in books_list:
                wr.writerow(each)

    @staticmethod
    def read_file():
        books_list = []
        if os.path.exists(Books.filename):
            with open(Books.filename, "r") as fp:
                rd = csv.DictReader(fp)
                for row in rd:
                    books_list.append(dict(row))

        return books_list

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

        books_list = Books.read_file()

        books_list.append({"name": name,
                           "author": author,
                           "read": read})

        Books.write_file(books_list)

    @classmethod
    def list_all_books(cls, books_list):
        if len(books_list) != 0:
            for book in books_list:
                Books.list_book_details(book)
        else:
            print("Books not found..")

    @staticmethod
    def list_book_details(book):
        print(f"Name : {book['name']}")
        print(f"Author : {book['author']}")
        print(f"Read : {book['read']}")

    @classmethod
    def search_book(cls):
        search_by = input("Search book by : ")
        looking_for = input("What are you looking for? : ")

        if looking_for.lower() == "true" or looking_for.lower() == "false":
            looking_for = str2bool(looking_for)
        
        books_list = Books.read_file()

        searched_book_list = Books.search_book_by_attribute(search_by, looking_for, books_list)
        if searched_book_list:
            cls.list_all_books(searched_book_list)
        else:
            print("Books not Found..")
        return searched_book_list

    @staticmethod
    def search_book_by_attribute(search_by, looking_for, book_list):
        try:
            filter_obj = filter(lambda x: str2bool(x[search_by]) == looking_for if search_by == "read"
                                else x[search_by] == looking_for
                                , book_list)
            searched_book_list = list(filter_obj)
        except KeyError:
            print("Search key not found.. Try again..")
            searched_book_list = []
        return searched_book_list

    @classmethod
    def delete_book(cls):
        searched_book_list = cls.search_book()

        books_list = Books.read_file()

        if len(searched_book_list) != 0:
            conf_del = input("R you sure u want to delete this Book? (y/n) : ")
            if conf_del == "y":
                for each in searched_book_list:
                    books_list.remove(each)
                Books.write_file(books_list)
                print("Deleted Successfully..")

    @classmethod
    def update_book_detail(cls):
        search_by = "name"
        looking_for = input("Enter a book name u want to edit : ")

        books_list = Books.read_file()
        searched_book_list = Books.search_book_by_attribute(search_by, looking_for, books_list)

        if len(searched_book_list) != 0:
            cls.list_all_books(searched_book_list)

            conf_update = input("R you sure u want to toggle the read flag of this Book? (y/n) : ")
            if conf_update == "y":
                for each in searched_book_list:
                    books_list[books_list.index(each)]['read'] = not \
                        str2bool(books_list[books_list.index(each)]['read'])

                Books.write_file(books_list)
                print("Updated Successfully..")
        else:
            print("Books not Found..")
