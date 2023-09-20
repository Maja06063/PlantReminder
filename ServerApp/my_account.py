from flask import render_template

def generate_my_account_page(args_dict, connection) -> str:

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM UserName WHERE login = '" + args_dict["login"] + "';")
    users = cursor.fetchall()

    # TODO pobieranie maila użytkownika oraz wstawianie loginu i maila

    return render_template("my_account.html")
