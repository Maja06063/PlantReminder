import mysql.connector
from flask import Flask

#Sprawdzenie połączenia z bazą
try:
    connection = mysql.connector.connect(
        host='localhost',
        user='sqluser',
        password='1234',
        database='plantreminderdb'
    )
    if connection.is_connected():
        print('Połączono z bazą danych!')

except mysql.connector.Error as e:
    print('Błąd połączenia z bazą danych:', e)

#Wypisanie danych z tabeli
try:
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM plants')

    rows = cursor.fetchall()

    for row in rows:
        print(row)

except mysql.connector.Error as e:
    print('Błąd przy wykonywaniu zapytania:', e)

#Tworzenie serwera http    

app = Flask(__name__)

@app.route('/')
def hello():
    return 'To będzie praca inżynierska PlantReminder. <a href=/Dane>Kliknij mnie<a/>'

@app.route('/Dane')
def dane():
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM plants')

    rows = cursor.fetchall()

    for i in range(0,len(rows)):
        rows[i]= str(rows[i])+'<br>'
    return str(rows)

if __name__ == '__main__':
    app.run(debug=True)


