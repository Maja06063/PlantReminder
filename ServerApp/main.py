from backend import Backend
from dbConector import DbConnector

#Tworzenie obiektu klasy backend i DbConector
backend = Backend()
db = DbConnector()

#Entry point - miejsce rozpoczęcia programu
if __name__ == "__main__":

    backend.add_database(db) # Dodaje bazę danych db do backendu.
    backend.prepare_endpoints() # Przygotowywuje flaskowe endpointy.
    backend.run() # Uruchomienie flaskowego serwera. Funkcja blokująca.
