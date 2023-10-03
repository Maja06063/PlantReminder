from hash import hash_password
from dbConector import base_commit
def userRegistered(post_data_dict) -> bool:
    
    hashed_password=hash_password(post_data_dict["password"])
    #zwraca czy udało się dodać do bazy danych (zarejestrować)
    is_success= base_commit("INSERT INTO username VALUES ('%s', '%s', '%s');" % (post_data_dict["login"], hashed_password, post_data_dict["email"]))
    return is_success
