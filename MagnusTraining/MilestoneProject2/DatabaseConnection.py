import mysql.connector


class DBConnect:

    def __init__(self):
        self._db_connection = mysql.connector.connect(host="localhost", user="root", passwd="password",
                                                      auth_plugin='mysql_native_password')
        self._db_connection.database = "book"
        self._db_cur = self._db_connection.cursor()

    def __del__(self):
        self._db_cur.close()
        self._db_connection.close()

    def insert_value(self, lst):
        try:
            for each in lst:
                sql = "INSERT INTO book_list (Book_Name, Author, Read_Flag) VALUES('%s', '%s', %i)" % each
                self._db_cur.execute(sql)

            self._db_connection.commit()

            print(self._db_cur.rowcount, "record inserted!")

        except mysql.connector.errors as e:
            self._db_connection.rollback()
            print(e)

    def search_value(self, *criteria):
        try:
            if len(criteria) == 2:
                if criteria[0] == "name":
                    sql = "SELECT * FROM book_list WHERE Book_Name = '%s'" % criteria[1]
                elif criteria[0] == "author":
                    sql = "SELECT * FROM book_list WHERE Author = '%s'" % criteria[1]
                elif criteria[0] == "read":
                    sql = "SELECT * FROM book_list WHERE Read_Flag = %i" % criteria[1]
                else:
                    sql = "SELECT * FROM book_list"
            else:
                sql = "SELECT * FROM book_list"

            self._db_cur.execute(sql)
            result = self._db_cur.fetchall()
            return result

        except mysql.connector.errors as e:
            self._db_connection.rollback()
            print(e)

    def delete_value(self, lst):
        try:
            for each in lst:
                sql = "DELETE FROM book_list WHERE Id = %d" % each[0]
                self._db_cur.execute(sql)

            self._db_connection.commit()
            print(self._db_cur.rowcount, "record delete!")
        except mysql.connector.errors as e:
            self._db_connection.rollback()
            print(e)

    def update_value(self, lst):
        try:
            for each in lst:
                sql = "UPDATE book_list SET Read_Flag = %i WHERE Id = %d" % (each[3], each[0])
                self._db_cur.execute(sql)

            self._db_connection.commit()
            print(self._db_cur.rowcount, "record updated!")
        except mysql.connector.errors as e:
            self._db_connection.rollback()
            print(e)

