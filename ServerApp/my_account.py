from flask import render_template

def generate_my_account_page(login, connection) -> str:

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM UserName WHERE login = '" + login + "';")
    users = cursor.fetchall()
    user = users[0]

    return render_template("my_account.html", login = user[0], email = user[2])

def generate_calendar_page(login, connection) -> str:

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM UserName WHERE login = '" + login + "';")
    users = cursor.fetchall()
    user = users[0]

    return render_template("calendar.html")
