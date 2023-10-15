from flask import render_template, make_response, Response
from plant import Plant
from datetime import date, timedelta
import json

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

        card = """
            <div class="card">
                <center>
                    <h2 class="no-bold-header">%s</h2>
                    <h3 class="Species-header">%s</h3>
                    <span style="display: block";> Następne podlewanie:Za <strong>%d</strong> dni</span>
                    <span style="display: block";> Następne nawożenie:Za <strong>%d</strong> dni</span>
                    <span style="display: block";> Następne wydarzenie:Za <strong>%d</strong> dni</span>
                    <p class="species-description">%s</p>
                    <button id="remove_plant_button" class="remove_plant_button" onclick="remove_plant(%d)">X</button>
                    <button id="edit_plant_button" onclick="redirect_to_add_plant(%d)">Edytuj</button>
                </center>
            </div>
            """ % (
                species_name,
                plant.name if plant.name != None else self.HTML_EMPTY_SPACE,
                self.days_to_care(plant.last_watered_date, plant.watering_period),
                self.days_to_care(plant.last_fertilized_date, plant.fertilization_period),
                -1,
                plant.description if plant.description != None else self.HTML_EMPTY_SPACE,
                plant.id,
                plant.id
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

    def generate_plant_form_page(self, plant_id:int) -> str:

        species = self.db.execute("SELECT * FROM Species;")

        if plant_id != 0:
            plants = self.db.execute("SELECT * FROM Plants WHERE plant_id = %d;"%plant_id)
            plant = Plant(plants[0])

        species_options = ""
        for one_specie in species:
            if plant_id != 0 and one_specie[0] == plant.species_id:
                species_options += """<option value="%d" selected>%s</option>\n""" % (one_specie[0], one_specie[1])
            else:
                species_options += """<option value="%d">%s</option>\n""" % (one_specie[0], one_specie[1])

        if plant_id==0:
            return render_template(
                "plant_card.html",
                available_species = species_options,
                onclick_function="save_new_plant()",
                button_text = "Dodaj roślinę"
                )


        if plant.name==None:
            plant.name=""
        if plant.description==None:
            plant.description=""
        return render_template(
            "plant_card.html",
            available_species = species_options,
            onclick_function="save_edited_plant()",
            button_text = "Edytuj roślinę",
            plant_name = plant.name,
            watering_period = plant.watering_period,
            fertiliz_period = plant.fertilization_period,
            plant_description = plant.description,
            last_watering = plant.last_watered_date,
            last_fertiliz = plant.last_fertilized_date
            )

    def generate_species_json(self, species_id) -> str:
        species_info = self.db.execute("SELECT * FROM species WHERE species_id = %d;"%int(species_id))
        print(species_info)
        species_dict = {"watering": species_info[0][2], "fertilization": species_info[0][3]}
        return json.dumps(species_dict)

    def plantAdded(self, login, post_data_dict) -> bool:

        #zwraca czy udało się dodać do bazy danych (zarejestrować)
        is_success = self.db.commit("""
            INSERT INTO Plants (
                login,
                plant_species,
                plant_name,
                watering_period,
                fertilization_period,
                last_watering_date,
                last_fertilization_date,
                plant_description
            ) VALUES ('%s', %d, '%s', %d, %d, '%s', '%s', '%s');""" %
            (
                login,
                int(post_data_dict["species"]),
                post_data_dict["plant_name"],
                int(post_data_dict["watering_period"]),
                int(post_data_dict["fertiliz_period"]),
                post_data_dict["last_watering"],
                post_data_dict["last_fertiliz"],
                post_data_dict["plant_description"]
            )
        )
        return is_success


    def plantEdited(self, login, post_data_dict) -> bool:
        print(post_data_dict["plant_id"])
        #zwraca czy udało się dodać do bazy danych (zarejestrować)

        is_success = self.db.commit("""
            UPDATE Plants
            SET plant_name = '%s',
            plant_species = %d,
            watering_period = %d,
            fertilization_period = %d,
            plant_description = '%s',
            last_watering_date = '%s',
            last_fertilization_date = '%s'
            WHERE plant_id = %d;""" % (
                post_data_dict["plant_name"],
                int(post_data_dict["species"]),
                int(post_data_dict["watering_period"]),
                int(post_data_dict["fertiliz_period"]),
                post_data_dict["plant_description"],
                post_data_dict["last_watering"],
                post_data_dict["last_fertiliz"],
                int(post_data_dict["plant_id"])
            )
        )
        return is_success