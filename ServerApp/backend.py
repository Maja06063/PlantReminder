from flask import Flask, request, render_template
from podstrona_login import generate_logged_page

app = Flask(__name__) #tworzenie nowej instancji klasy Flask

@app.route('/')
def initial_web_page():
    return render_template("index.html")

@app.route('/podstrona_login', methods=['POST'])
def logged_page():
    args = request.args
    return generate_logged_page(args)

if __name__ == '__main__':
    app.run(debug=True)
