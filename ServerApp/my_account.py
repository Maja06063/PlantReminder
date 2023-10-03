from flask import render_template
from dbConector import base_execute

def generate_my_account_page(login) -> str:

    users = base_execute("SELECT * FROM UserName WHERE login = '" + login + "';")
    user = users[0]

    return render_template("my_account.html", login = user[0], email = user[2])

def generate_calendar_page(login) -> str:

    users = base_execute("SELECT * FROM UserName WHERE login = '" + login + "';")
    user = users[0]

    return render_template("calendar.html")
