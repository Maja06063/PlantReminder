from backend import Backend
from dbConector import DbConnector

import argparse

def get_args():
    parser = argparse.ArgumentParser(description="Uruchamianie aplikacji Plant Reminder")

    parser.add_argument(
        "-p" ,"--port",
        type=int,
        default=5000,
        help="Port sieciowy Flask (domyślnie 5000)"
    )

    parser.add_argument(
        "-d", "--db",
        type=str,
        default="plantreminderdb",
        help="Nazwa bazy danych (domyślnie plantreminderdb)"
    )

    return parser.parse_args()

#Entry point - miejsce rozpoczęcia programu
if __name__ == "__main__":

    args = get_args()

    #Tworzenie obiektu klasy backend i DbConector
    backend = Backend(args.port)
    db = DbConnector(args.db)

    backend.add_database(db) # Dodaje bazę danych db do backendu.
    backend.prepare_endpoints() # Przygotowywuje flaskowe endpointy.
    backend.run() # Uruchomienie flaskowego serwera. Funkcja blokująca.
