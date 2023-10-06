import hashlib

class Hasher:

    @staticmethod
    def hash_password(password):

        # Tworzenie obiektu haszującego MD5
        md5 = hashlib.md5()

        # Dodawanie hasła do obiektu haszującego
        md5.update(password.encode('utf-8'))

        # Pobieranie zahaszowanego hasła jako ciąg znaków szesnastkowych
        hashed_password = md5.hexdigest()

        return hashed_password
