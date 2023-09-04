from flask import Flask, request, render_template
from podstrona_login import generate_logged_page
from dbConector import base_connect

app = Flask(__name__) #tworzenie nowej instancji klasy Flask

@app.route('/')
def initial_web_page():
    return render_template("index.html")

@app.route('/podstrona_login', methods=['POST'])
def logged_page():
    post_data_dict = request.form.to_dict()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM UserName WHERE login = '" + post_data_dict["login"] + "';")
    
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    return generate_logged_page(post_data_dict)

if __name__ == '__main__':
    connection = base_connect()
    app.run(debug=True)
