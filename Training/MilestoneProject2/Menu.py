# from MilestoneProject2.BooksLibraryWithList import Books
# from MilestoneProject2.BooksLibraryWithJSON import Books
from MilestoneProject2.BooksLibraryWithCSV import Books
# from MilestoneProject2.BooksLibraryWithDB import Books
# from MilestoneProject2.DatabaseConnection import DBConnect


def menu():
    book = Books()
    while True:
        menu_selection = input(
            "Enter \'a\' to \'Add a book\' | \'l\' to \'List all the books\' | \'s\' to \'Search a book\' | "
            "\'d\' to \'Delete a book\' | \'u\' to \'Update a book detail\' | \'q\' to \'Quit\' : ")

        if menu_selection == 'q':
            break
        elif menu_selection == 'a':
            book.add_new_book()
        elif menu_selection == 'l':
            # FOR LIST : comment out code below and comment rest
                # book.list_all_books(book.books_list)

            # FOR CSV/JSON : comment out code below and comment rest
            books_list = book.read_file()
            book.list_all_books(books_list)

            # FOR DATABASE : comment out code below and comment rest
                # dbconnect = DBConnect()
                # books_list = dbconnect.search_value()
                # book.list_all_books(books_list)
        elif menu_selection == 's':
            book.search_book()
        elif menu_selection == 'd':
            book.delete_book()
        elif menu_selection == 'u':
            book.update_book_detail()
        else:
            print("Unknown command..")


menu()

