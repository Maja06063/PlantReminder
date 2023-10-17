import mysql.connector
"""
Klasa DbConnector służy się do połączenia się aplikacji serwerowej z bazą danych MySQL
"""
class DbConnector():

    #Sprawdzenie połączenia z bazą
    def __init__(self) -> None:
        
        self.connection = None

        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                user='sqluser',
                password='1234',
                database='plantreminderdb'
            )
            if self.connection.is_connected():
                print("Database connected")

        except mysql.connector.Error as e:
            print("Database connection error: ", e)
            
    # ODCZYT Z BAZY DANYCH
    # Wykonanie polecenia sql w bazie danych i zwrócenie wyniku w postaci listy wierszy
    def execute(self, sql: str) -> list:

        cursor = self.connection.cursor()
        cursor.execute(sql)
        return cursor.fetchall()
    #ZAPIS DO BAZYU DANYCH
    # Wykonanie polecenia sql zmieniającego bazę danych:
    def commit(self, sql: str) -> bool:

        cursor = self.connection.cursor()
        try:
            cursor.execute(sql)
            self.connection.commit()
        except:
            return False

        return True
