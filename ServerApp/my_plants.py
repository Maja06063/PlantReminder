from flask import render_template, make_response, Response
from plant import Plant
from datetime import date, timedelta

class MyPlantsPageGenerator():

    HTML_EMPTY_SPACE = "&nbsp;"

    def add_database(self, db_to_add):
        self.db = db_to_add

    def days_to_care(self, last_action_date, days_to_add) -> int:

        delta = timedelta(days=days_to_add)
        today = date.today()
        result = int((last_action_date + delta - today).days)

        return result if result > 0 else 0

    def generate_one_card(self, plant_list) -> str:

        plant = Plant(plant_list)
        species = self.db.execute("SELECT * FROM Species WHERE species_id = '" + str(plant.species_id)+ "';")
        species = list(species[0])
        species_name = species[1]

        if plant.watering_period == None:
            plant.watering_period = species[2]
        if plant.fertilization_period == None:
            plant.fertilization_period = species[3]
        if plant.light == None:
            plant.light = species[4]

        card = """
            <div class="card">
                <center>
                    <h2 class="no-bold-header">%s</h2>
                    <h3 class="Species-header">%s</h3>
                    <span style="display: block";> Następne podlewanie:Za <strong>%d</strong> dni</span>
                    <span style="display: block";> Następne nawożenie:Za <strong>%d</strong> dni</span>
                    <span style="display: block";> Następne wydarzenie:Za <strong>%d</strong> dni</span>
                    <p class="species-description">%s</p>
                </center>
            </div>
            """ % (
                species_name,
                plant.name if plant.name != None else self.HTML_EMPTY_SPACE,
                self.days_to_care(plant.last_watered_date, plant.watering_period),
                self.days_to_care(plant.last_fertilized_date, plant.fertilization_period),
                plant.light,
                plant.description if plant.description != None else self.HTML_EMPTY_SPACE,
            )

        return card

    def generate_plants_cards(self, plants) -> str:

        cards = ""
        for plant in plants:
            cards += self.generate_one_card(list(plant))

        return cards

    def generate_logged_page(self, args_dict) -> Response:

        plants = self.db.execute("SELECT * FROM Plants WHERE login = '" + args_dict["login"] + "';")

        page_str = render_template("my_plants.html", plants_cards = self.generate_plants_cards(plants))

        response = make_response(page_str)
        response.set_cookie('login', args_dict["login"])
        return response

    def generate_plants_page(self, login) -> str:

        plants = self.db.execute("SELECT * FROM Plants WHERE login = '" + login + "';")

        return render_template("my_plants.html", plants_cards = self.generate_plants_cards(plants))

    def generate_new_plant_form_page(self) -> str:

        species = self.db.execute("SELECT * FROM Species;")

        species_options = ""
        for one_specie in species:
            species_options += """<option value="%d">%s</option>\n""" % (one_specie[0], one_specie[1])

        return render_template("plant_card.html", available_species = species_options)
