from flask import render_template
from hash import Hasher

"""
Klasa, która zajmuje się generowaniem stron związanych z kontem użytkownika
"""
class AccountPagesGenerator:
    # stworzenie obiektu hashera, aby użyć potem jego metody do haszowania
    hasher = Hasher()

    #Zapisuje odpowiednie połączenie z bazą danych, aby używać go w innych metodach
    #daje dostęp do dbConectora
    def add_database(self, db_to_add):
        self.db = db_to_add

    #generuje podstornę mojekonto na podstawie pliku html dla odpowiedniego użytkownika
    # umieszcza na tej stronie jego login oraz mail
    def generate_my_account_page(self, login) -> str:

        users = self.db.execute("SELECT * FROM UserName WHERE login = '%s';" % login)
        user = users[0]

        return render_template("my_account.html", login = user[0], email = user[2])


    #metoda wysyła do bazy danych żądanie dodanie nowego użytkownika do bazy danych o podanym loginie, mailu oraz zahaszowanym haśle
    def userRegistered(self, post_data_dict) -> bool:

        hashed_password = self.hasher.hash_password(post_data_dict["password"])
        #zwraca czy udało się dodać do bazy danych (zarejestrować)
        is_success = self.db.commit("INSERT INTO username VALUES ('%s', '%s', '%s');" %
                                    (
                                        post_data_dict["login"],
                                        hashed_password, 
                                        post_data_dict["email"]
                                    ))        
        return is_success

