from flask import Flask, request, render_template, make_response
from podstrona_login import generate_logged_page, generate_plants_page, generate_new_plant_form_page
from my_account import generate_my_account_page, generate_calendar_page
from dbConector import base_commit, base_execute
from users import userRegistered
import json
from hash import hash_password

app = Flask(__name__) #tworzenie nowej instancji klasy Flask

@app.route('/')
def initial_web_page():
    return render_template("index.html")

@app.route('/podstrona_login', methods=['GET'])
def redirect_to_plants_page():
    try:
        rows = base_execute("SELECT * FROM UserName WHERE login = '" + request.cookies.get("login") + "';")
    except(TypeError):
        return "<script>location.href = '/';</script>"
    if (len(rows) == 1): #Sprawdzamy czy znaleziono uzytkownika o podany loginie
        return generate_plants_page(request.cookies.get("login"))

    return "<script>location.href = '/';</script>"

@app.route('/my_account', methods=['GET'])
def redirect_to_my_account_page():

    rows = base_execute("SELECT * FROM UserName WHERE login = '" + request.cookies.get("login") + "';")

    if (len(rows) == 1): #Sprawdzamy czy znaleziono uzytkownika o podany loginie
        return generate_my_account_page(request.cookies.get("login"))

    return "<script>location.href = '/';</script>"

@app.route('/my_account', methods=['POST'])
def change_password_endpoint():

    post_data_dict = request.form.to_dict()
    rows = base_execute("SELECT * FROM UserName WHERE login = '" + request.cookies.get("login") + "';")

    if len(rows) == 1: #Sprawdzamy czy znaleziono uzytkownika o podany loginie

        #sprawdzamy czy actual_pass się zgadza
        hashed_actual_password=hash_password(str(post_data_dict["actual_pass"]))
        if str(rows[0][1])==hashed_actual_password: 
            #sprawdzamy czy new_pass i confirm_pass są takie same
            if post_data_dict["new_pass"]==post_data_dict["confirm_pass"]:
                #zmieniamy hasło w bazie danych
                hashed_new_password=hash_password(str(post_data_dict["new_pass"]))
                if base_commit("UPDATE UserName SET password = '%s' WHERE login = '%s';" % (hashed_new_password, request.cookies.get("login"))):
                    
                    return generate_my_account_page(request.cookies.get("login")) + """<script>alert("Hasło zmienione")</script>"""

        return generate_my_account_page(request.cookies.get("login")) + """<script>alert("Zmiana hasła nieudana!")</script>"""

    return "<script>location.href = '/';</script>"
@app.route('/calendar', methods=['GET'])
def redirect_to_calendar_page():

    rows = base_execute("SELECT * FROM UserName WHERE login = '" + request.cookies.get("login") + "';")

    if (len(rows) == 1): #Sprawdzamy czy znaleziono uzytkownika o podany loginie
        return generate_calendar_page(request.cookies.get("login"))

    return "<script>location.href = '/';</script>"

@app.route('/plant_card', methods=['GET'])
def redirect_to_plant_card_page():
    return generate_new_plant_form_page()

@app.route('/podstrona_sign', methods=['GET','POST'])
def redirect_to_sign_page():
    return render_template("podstrona_sign.html")

@app.route('/register', methods=['POST'])
def register_endpoint():
    post_data_dict = request.form.to_dict()
    if userRegistered(post_data_dict):
        return render_template("index.html") + """
            <script>var regist_ok = document.getElementById("regist_ok");
            regist_ok.style.display = "block";</script>
            """
    else:
        return "Rejestracja nie udana"

@app.route('/forgot_password', methods=['GET'])
def redirect_to_forgot_password():
    return render_template("forgot_password.html")

@app.route('/podstrona_login', methods=['POST'])
def logged_page():

    post_data_dict = request.form.to_dict()
    rows = base_execute("SELECT * FROM UserName WHERE login = '" + post_data_dict["login"] + "';")

    if len(rows) == 1: #Sprawdzamy czy znaleziono uzytkownika o podany loginie
        hashed_password=hash_password(str(post_data_dict["password"]))
        if str(rows[0][1])==hashed_password: #Sprawdzamy czy zgadza sie haslo
            return generate_logged_page(post_data_dict) #funkcja zwraca gotowa strone

        return render_template("index.html") + """
            <script>var pass_error = document.getElementById("pass_error");
            pass_error.style.display = "block";</script>
            """

    return render_template("index.html") + """
        <script>var login_error = document.getElementById("login_error");
        login_error.style.display = "block";</script>
        """

if __name__ == '__main__':
    app.run()
