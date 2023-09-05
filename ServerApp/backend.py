from flask import Flask, request, render_template
from podstrona_login import generate_logged_page
from dbConector import base_connect

app = Flask(__name__) #tworzenie nowej instancji klasy Flask

@app.route('/')
def initial_web_page():
    return render_template("index.html")

@app.route('/podstrona_login', methods=['GET'])
def redirect_to_login_page():
    return "<script>location.href = '/';</script>"


@app.route('/podstrona_login', methods=['POST'])
def logged_page():
    post_data_dict = request.form.to_dict()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM UserName WHERE login = '" + post_data_dict["login"] + "';")
    rows = cursor.fetchall()

    if (len(rows) == 1):

        if (str(rows[0][1])==str(post_data_dict["password"])):
            return generate_logged_page(post_data_dict, connection)

        return render_template("index.html") + """
            <script>var pass_error = document.getElementById("pass_error");
            pass_error.style.display = "block";</script>
            """

    return render_template("index.html") + """
        <script>var login_error = document.getElementById("login_error");
        login_error.style.display = "block";</script>
        """

if __name__ == '__main__':
    connection = base_connect()
    app.run()
