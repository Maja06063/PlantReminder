from flask import Flask, request, render_template, make_response
from my_plants import MyPlantsPageGenerator
from my_account import AccountPagesGenerator
from hash import Hasher

class Backend():

    app = Flask(__name__) #tworzenie nowej instancji klasy Flask
    my_plants_gen = MyPlantsPageGenerator()
    accounts_pages_gen = AccountPagesGenerator()

    def prepare_endpoints(self):

        #############################################################
        ################ STRONY STATYCZNE ###########################
        #############################################################

        @self.app.route('/')
        def index_page():
            return render_template("index.html")

        @self.app.route('/register_page', methods=['GET','POST'])
        def register_page():
            return render_template("register_page.html")

        @self.app.route('/forgot_password', methods=['GET'])
        def forgot_password_page():
            return render_template("forgot_password.html")

        #############################################################
        ################ ENDPOINT REJESTRACJI #######################
        #############################################################

        @self.app.route('/register', methods=['POST'])
        def register_endpoint():
            post_data_dict = request.form.to_dict()
            if self.accounts_pages_gen.userRegistered(post_data_dict):
                return render_template("index.html") + """
                    <script>document.getElementById("regist_ok").style.display = "block";</script>
                    """
            else:
                return "Rejestracja nie udana"

        #############################################################
        ################ PODSTRONA MY_ACCOUNT #######################
        #############################################################

        @self.app.route('/my_account', methods=['GET'])
        def my_account_endpoint():

            rows = self.db.execute("SELECT * FROM UserName WHERE login = '" + request.cookies.get("login") + "';")

            if (len(rows) == 1): #Sprawdzamy czy znaleziono uzytkownika o podany loginie
                return self.accounts_pages_gen.generate_my_account_page(request.cookies.get("login"))

            return "<script>location.href = '/';</script>"

        @self.app.route('/my_account', methods=['POST'])
        def change_password_endpoint():

            post_data_dict = request.form.to_dict()
            rows = self.db.execute("SELECT * FROM UserName WHERE login = '" + request.cookies.get("login") + "';")

            if len(rows) == 1: #Sprawdzamy czy znaleziono uzytkownika o podany loginie

                #sprawdzamy czy actual_pass się zgadza
                hashed_actual_password = Hasher.hash_password(str(post_data_dict["actual_pass"]))
                if str(rows[0][1])==hashed_actual_password:
                    #sprawdzamy czy new_pass i confirm_pass są takie same
                    if post_data_dict["new_pass"]==post_data_dict["confirm_pass"]:
                        #zmieniamy hasło w bazie danych
                        hashed_new_password = Hasher.hash_password(str(post_data_dict["new_pass"]))
                        if self.db.commit("UPDATE UserName SET password = '%s' WHERE login = '%s';" % (hashed_new_password, request.cookies.get("login"))):

                            return self.accounts_pages_gen.generate_my_account_page(request.cookies.get("login")) + """<script>alert("Hasło zmienione")</script>"""

                return self.accounts_pages_gen.generate_my_account_page(request.cookies.get("login")) + """<script>alert("Zmiana hasła nieudana!")</script>"""

            return "<script>location.href = '/';</script>"

        #############################################################
        ################ PODSTRONA MY_PLANTS ########################
        #############################################################

        @self.app.route('/my_plants', methods=['GET'])
        def my_plants_endpoint():
            try:
                rows = self.db.execute("SELECT * FROM UserName WHERE login = '" + request.cookies.get("login") + "';")
            except(TypeError):
                return "<script>location.href = '/';</script>"
            if (len(rows) == 1): #Sprawdzamy czy znaleziono uzytkownika o podany loginie
                return self.my_plants_gen.generate_plants_page(request.cookies.get("login"))

            return "<script>location.href = '/';</script>"

        @self.app.route('/my_plants', methods=['POST'])
        def logging_endpoint():

            post_data_dict = request.form.to_dict()
            rows = self.db.execute("SELECT * FROM UserName WHERE login = '" + post_data_dict["login"] + "';")

            if len(rows) == 1: #Sprawdzamy czy znaleziono uzytkownika o podany loginie
                hashed_password = Hasher.hash_password(str(post_data_dict["password"]))
                if str(rows[0][1])==hashed_password: #Sprawdzamy czy zgadza sie haslo
                    return self.my_plants_gen.generate_logged_page(post_data_dict) #funkcja zwraca gotowa strone

                return render_template("index.html") + """
                    <script>document.getElementById("pass_error").style.display = "block";</script>
                    """

            return render_template("index.html") + """
                <script>document.getElementById("login_error").style.display = "block";</script>
                """

        @self.app.route('/plant_card', methods=['GET'])
        def add_plant_endpoint():
            return self.my_plants_gen.generate_new_plant_form_page()

        #############################################################
        ################ PODSTRONA CALENDAR #########################
        #############################################################

        @self.app.route('/calendar', methods=['GET'])
        def redirect_to_calendar_page():

            rows = self.db.execute("SELECT * FROM UserName WHERE login = '" + request.cookies.get("login") + "';")

            if (len(rows) == 1): #Sprawdzamy czy znaleziono uzytkownika o podany loginie
                return self.accounts_pages_gen.generate_calendar_page(request.cookies.get("login"))

            return "<script>location.href = '/';</script>"

    #############################################################
    ################ METODY PUBLICZNE ###########################
    #############################################################

    def run(self):
        self.app.run()

    def add_database(self, db_to_add):
        self.db = db_to_add
        self.my_plants_gen.add_database(db_to_add)
        self.accounts_pages_gen.add_database(db_to_add)
