"""
Klasa ta służy do przechowywania informacji o danej roślinie.
Po wyciągnięciu z bazy danych roślina jest listą, a ta klasa pozwala na używanie
roślin jako obiektów.
"""
class Plant:
    """
    Konstruktor klasy Plant. Jako argument przyjmuje on roślinę w postaci listy
    i przekształca w obiekt.
    """
    def __init__(self, plant_list: list):
        
        self.id = int(plant_list[0])
        self.owner = plant_list[1]
        self.species_id = int(plant_list [2])
        self.name = plant_list[3]
        self.watering_period = plant_list[4]
        self.fertilization_period = plant_list[5]
        self.description = plant_list[6]
        self.last_watered_date = plant_list[7]
        self.last_fertilized_date = plant_list[8]

    """
    Metoda iterująca. Konwertuje roślinę na listę.
    """
    def __iter__(self):
        return iter([
            self.id,
            self.owner,
            self.species_id,
            self.name,
            self.watering_period,
            self.fertilization_period,
            self.description,
            self.last_watered_date,
            self.last_fertilized_date
        ])
