import mysql.connector

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
