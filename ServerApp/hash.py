import hashlib

"""
Klasa Hasher haszuje podany string metodą hash_password za pomocą algorytmu md5
"""
class Hasher:

    def hash_password(self, str_password):

        # Tworzenie obiektu typu md5 o nazwie md5
        md5 = hashlib.md5()

        # Wyliczenie hasha z podanego tekstu
        md5.update(str_password.encode('utf-8'))

        #Przekształcenie hasha na formę 16-nastkową
        hashed_password = md5.hexdigest()

        return hashed_password
