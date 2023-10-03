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
def base_execute(sql:str)->list: # wykonanie polecenia sql w bazie danych i zwrócenie wyniku w postaci listy wierszy
    cursor = connection.cursor()
    cursor.execute(sql)
    return cursor.fetchall()

def base_commit(sql:str)->bool:

    cursor = connection.cursor()
    try:
        cursor.execute(sql)
        connection.commit()
    except:
        return False

    return True


connection = base_connect()
