import unittest
from hash import Hasher
from dbConector import DbConnector
from backend import Backend
from plant import Plant
from my_plants import MyPlantsPageGenerator
from datetime import date

class TestApp(unittest.TestCase):

    def test_hash(self):
        hasher = Hasher()
        self.assertEqual(hasher.hash_password("alamakota1"), "0099c0edac533c3e3a7a43874c8af9e8")

    def test_database_connection(self):
        dbconnector = DbConnector()
        tables = dbconnector.execute("SHOW TABLES;")
        self.assertTrue(tables)

    def test_adding_database_to_backend(self):
        dbconnector = DbConnector()
        backend = Backend()
        backend.add_database(dbconnector)
        self.assertEqual(backend.db, dbconnector)

    def test_plant(self):
        plant = Plant([
            1,
            "Danuta",
            2,
            "w salonie",
            4,
            6,
            "Podlewać od dołu.",
            "2023-11-20",
            "2023-11-19"
        ])
        for feature in plant:
            self.assertNotEqual(feature, None)

    def test_days_to_care_today(self):
        my_plants_page_generator = MyPlantsPageGenerator()
        self.assertEqual(my_plants_page_generator.days_to_care(date.today(), 3), 3)

    def test_days_to_care_past(self):
        my_plants_page_generator = MyPlantsPageGenerator()
        self.assertEqual(my_plants_page_generator.days_to_care(date(2020, 1, 1), 3), 0)

if __name__ == '__main__':
    unittest.main()