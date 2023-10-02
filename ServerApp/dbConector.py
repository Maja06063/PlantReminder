import mysql.connector

#Sprawdzenie połączenia z bazą
def base_connect():
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
    return connection
