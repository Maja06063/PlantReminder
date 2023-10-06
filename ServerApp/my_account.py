from flask import render_template
from hash import Hasher

class AccountPagesGenerator():

    def add_database(self, db_to_add):
        self.db = db_to_add

    def generate_my_account_page(self, login) -> str:

        users = self.db.execute("SELECT * FROM UserName WHERE login = '%s';" % login)
        user = users[0]

        return render_template("my_account.html", login = user[0], email = user[2])

    def generate_calendar_page(self, login) -> str:

        users = self.db.execute("SELECT * FROM UserName WHERE login = '%s';" % login)
        user = users[0]

        return render_template("calendar.html")

    def userRegistered(self, post_data_dict) -> bool:

        hashed_password = Hasher.hash_password(post_data_dict["password"])
        #zwraca czy udało się dodać do bazy danych (zarejestrować)
        is_success = self.db.commit("INSERT INTO username VALUES ('%s', '%s', '%s');" %
                                    (
                                        post_data_dict["login"],
                                        hashed_password, 
                                        post_data_dict["email"]
                                    ))        
        return is_success
