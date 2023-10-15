from flask import Flask, request, render_template, make_response
from my_plants import MyPlantsPageGenerator
from my_account import AccountPagesGenerator
from hash import Hasher

class Backend():

    app = Flask(__name__) #tworzenie nowej instancji klasy Flask
    my_plants_gen = MyPlantsPageGenerator()
    accounts_pages_gen = AccountPagesGenerator()
    hasher=Hasher()

    def prepare_endpoints(self):

        #############################################################
        ################ STRONY STATYCZNE ###########################
        #############################################################

        # Wejście na stronę główną:
        @self.app.route('/')
        def index_page():
            return render_template("index.html")

        # Wejście na stronę z rejestracją:
        @self.app.route('/register_page', methods=['GET','POST'])
        def register_page():
            return render_template("register_page.html")

        # Wejście na stronę z odzyskiwaniem hasła:
        @self.app.route('/forgot_password', methods=['GET'])
        def forgot_password_page():
            return render_template("forgot_password.html")

        #############################################################
        ################ ENDPOINT REJESTRACJI #######################
        #############################################################

        # Po wpisaniu danych rejestracji i kliknięciu przycisku "zajejestruj":
        @self.app.route('/register', methods=['POST'])
        def register_endpoint():
            post_data_dict = request.form.to_dict()#zamiana formularzu na pythonowy słownik
            # Ten if zostanie wykonany, jeśli rejestracja użytkownika się udała:
            if self.accounts_pages_gen.userRegistered(post_data_dict):
                #zwraca plik index.html wraz ze skryptem włączającym banner, że rejestracja się udała
                return render_template("index.html") + """
                    <script>document.getElementById("regist_ok").style.display = "block";</script>
                    """
            else:
                return "Rejestracja nie udana"

        #############################################################
        ################ PODSTRONA MY_ACCOUNT #######################
        #############################################################

        # Wejście na podstronę "moje konto" po zalogowaniu się:
        @self.app.route('/my_account', methods=['GET'])
        def my_account_endpoint():
            # Po wykonaniu poniższej linii rows zawiera listę użytkowników o loginie odczytanym z ciasteczka "login":
            rows = self.db.execute("SELECT * FROM UserName WHERE login = '" + request.cookies.get("login") + "';")

            if (len(rows) == 1): #Sprawdzamy czy znaleziono uzytkownika o podany loginie
                # Jeżeli znaleźliśmy użytkownika, zwracamy dostosowaną pod niego stronę (z jego danymi):
                return self.accounts_pages_gen.generate_my_account_page(request.cookies.get("login"))

            return "<script>location.href = '/';</script>" # Jeśli nie, to przekierowywujemy na stronę główną

        # Po wpisaniu starego hasła oraz 2 razy nowego i kliknięciu "zmień hasło":
        @self.app.route('/my_account', methods=['POST'])
        def change_password_endpoint():

            post_data_dict = request.form.to_dict()#zamiana formularzu na pythonowy słownik
            # Po wykonaniu poniższej linii rows zawiera listę użytkowników o loginie odczytanym z ciasteczka "login":
            rows = self.db.execute("SELECT * FROM UserName WHERE login = '" + request.cookies.get("login") + "';")

            if len(rows) == 1: #Sprawdzamy czy znaleziono uzytkownika o podany loginie

                #sprawdzamy czy actual_pass się zgadza 
                # (hashujemy hasło przez użytkownika i sprawdzamy czy hash z tg wprowadzonego hasła pasuje z hashem z bazy danych)
                hashed_actual_password = self.hasher.hash_password(str(post_data_dict["actual_pass"]))
                if str(rows[0][1])==hashed_actual_password:
                    #sprawdzamy czy new_pass i confirm_pass są takie same
                    if post_data_dict["new_pass"]==post_data_dict["confirm_pass"]:
                        #zmieniamy hasło w bazie danych
                        hashed_new_password = self.hasher.hash_password(str(post_data_dict["new_pass"]))
                        #zmiana hasła w bazie danych
                        if self.db.commit("UPDATE UserName SET password = '%s' WHERE login = '%s';" % (hashed_new_password, request.cookies.get("login"))):

                            return self.accounts_pages_gen.generate_my_account_page(request.cookies.get("login")) + """<script>alert("Hasło zmienione")</script>"""
                # jesli ktorys z 3 ifow sie nie uda, trafia tutaj
                return self.accounts_pages_gen.generate_my_account_page(request.cookies.get("login")) + """<script>alert("Zmiana hasła nieudana!")</script>"""

            return "<script>location.href = '/';</script>"

        #############################################################
        ################ PODSTRONA MY_PLANTS ########################
        #############################################################

        # Wejście na podstronę "moje rośliny" po zalogowaniu się:
        @self.app.route('/my_plants', methods=['GET'])
        def my_plants_endpoint():
            try:
                # Po wykonaniu poniższej linii rows zawiera listę użytkowników o loginie odczytanym z ciasteczka "login":
                rows = self.db.execute("SELECT * FROM UserName WHERE login = '" + request.cookies.get("login") + "';")
            except(TypeError):
                #jak napotka ten error, to wraca do strony do logowania
                return "<script>location.href = '/';</script>"
            if (len(rows) == 1): #Sprawdzamy czy znaleziono uzytkownika o podany loginie
                return self.my_plants_gen.generate_plants_page(request.cookies.get("login"))

            return "<script>location.href = '/';</script>"

        # Po wpisaniu loginu i hasła oraz kliknięciu "zaloguj":
        @self.app.route('/my_plants', methods=['POST'])
        def logging_endpoint():

            post_data_dict = request.form.to_dict()
            rows = self.db.execute("SELECT * FROM UserName WHERE login = '" + post_data_dict["login"] + "';")

            if len(rows) == 1: #Sprawdzamy czy znaleziono uzytkownika o podany loginie
                hashed_password = self.hasher.hash_password(str(post_data_dict["password"]))#hashujemy haslo podane przez uzytkownika
                if str(rows[0][1])==hashed_password: #Sprawdzamy czy zgadza sie hash podany przez uzytkownika z tym w bazie danych
                    return self.my_plants_gen.generate_logged_page(post_data_dict) #funkcja zwraca gotowa strone moje rosliny

                #jesli poda bledne haslo to wyskoczy okienko o podanym blednym hasle
                return render_template("index.html") + """
                    <script>document.getElementById("pass_error").style.display = "block";</script>
                    """
            #jesli poda bledny login to wyskoczy okienko o podanym blednym loginie
            return render_template("index.html") + """
                <script>document.getElementById("login_error").style.display = "block";</script>
                """

        # Po kliknięciu "dodaj roślinę lub edytuj roślinę":
        @self.app.route('/plant_card', methods=['GET'])
        def add_plant_endpoint():
            plant_id = request.args.get("plant_id")
            return self.my_plants_gen.generate_plant_form_page(int(plant_id))
        
        @self.app.route('/get_species_data', methods=['GET'])
        def get_species_data_endpoint(): 
            species_id = request.args.get("species_id")
            return self.my_plants_gen.generate_species_json(species_id)
        
        @self.app.route('/save_plant', methods=["POST"])
        def add_new_plant_endpoint():
            post_data_dict = request.get_json()
            if self.my_plants_gen.plantAdded(request.cookies.get("login"), post_data_dict):
                return make_response("", 201)
            else:
                return make_response("", 400)
            
        @self.app.route('/save_plant', methods=["PUT"])
        def edit_plant_endpoint():
            post_data_dict = request.get_json()
            if self.my_plants_gen.plantEdited(request.cookies.get("login"), post_data_dict):
                return make_response("", 201)
            else:
                return make_response("", 400)
            
        @self.app.route('/remove_plant', methods=["DELETE"])
        def remove_plant_endpoint():
            post_data_dict = request.get_json()
            if self.db.commit("DELETE FROM Plants WHERE plant_id = %d;" % post_data_dict["plant_id"]):
                return make_response("", 204)
            else:
                return make_response("", 400)

        #############################################################
        ################ PODSTRONA CALENDAR #########################
        #############################################################

        # Wejście na podstronę kalendarza po zalogowaniu:
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
