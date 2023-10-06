from backend import Backend
from dbConector import DbConnector

backend = Backend()
db = DbConnector()

if __name__ == "__main__":

    backend.add_database(db)
    backend.prepare_endpoints()
    backend.run()