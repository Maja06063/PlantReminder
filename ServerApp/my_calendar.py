from flask import render_template
import json

"""
Klasa, która zajmuje się generowaniem stron związanych z kalenadarzem
"""
class CalendarPagesGenerator:

    #Zapisuje odpowiednie połączenie z bazą danych, aby używać go w innych metodach
    #daje dostęp do dbConectora
    def add_database(self, db_to_add):
        self.db = db_to_add


    # generuje podstornę kalendarz na podstawie pliku html dla odpowiedniego użytkownika
    def generate_calendar_page(self, login) -> str:

        users = self.db.execute("SELECT * FROM UserName WHERE login = '%s';" % login)
        user = users[0]

        return render_template("calendar.html")
    

    def get_user_events(self, login: str) -> str:
        events = self.db.execute("SELECT * FROM EventsOfUsers WHERE login='%s';"%login)
        events_list=[]
        for event in events:
            event=list(event)
            event[3]=str(event[3])
            events_list.append(event)

        return json.dumps(events_list)
    
    def generate_event_form_page(self, event_id: int, date: str, login: str):

        names_species = self.db.execute("SELECT * FROM PlantNamesSpecies WHERE login='%s';"%login)

        if event_id != 0:
            events = self.db.execute("SELECT * FROM SpecialEvent WHERE special_event_id = %d;"%event_id)
            event = events[0]

        plant_names_species_options = ""
        for one_name_specie in names_species:
            if event_id != 0 and one_name_specie[0] == event[1]:
                plant_names_species_options += """<option value="%d" selected>%s %s</option>\n""" % (
                    one_name_specie[0],
                    ""if one_name_specie[2]==None else one_name_specie[2],
                    one_name_specie[3])
            else:
                plant_names_species_options += """<option value="%d">%s %s</option>\n""" % (
                    one_name_specie[0],
                    ""if one_name_specie[2]==None else one_name_specie[2],
                    one_name_specie[3])

        date = "%d-%d-%d"%(int(date[0]),int(date[1]), int(date[2]))
        if event_id == 0:
            return render_template(
                "event_form.html",
                available_names_species = plant_names_species_options ,
                date = date,
                onclick_function="save_new_event()",
                button_text = "Dodaj wydarzenie"
                )

        return render_template(
            "event_form.html",
            event_name = event[2],
            event_description = event[3],
            available_names_species = plant_names_species_options ,
            date = date,
            onclick_function="save_edited_event()",
            button_text = "Edytuj wydarzenie",
            )

    def eventAdded(self, login, post_data_dict) -> bool:

        #zwraca czy udało się dodać do bazy danych (zarejestrować)
        is_success = self.db.commit("""
            INSERT INTO SpecialEvent (
                plant_id,
                event_name,
                event_description,
                event_date
            ) VALUES (%d, '%s', '%s', '%s');""" %
            (
                int(post_data_dict["plant_id"]),
                post_data_dict["event_name"],
                post_data_dict["event_description"],
                post_data_dict["event_date"]
            )
        )
        return is_success


    def eventEdited(self, login, post_data_dict) -> bool:

        is_success = self.db.commit("""
            UPDATE SpecialEvent
            SET plant_id = %d,
            event_name = '%s',
            event_description = '%s'                       
            WHERE special_event_id = %d;""" % (
                int(post_data_dict["plant_id"]),
                post_data_dict["event_name"],
                post_data_dict["event_description"],
                int(post_data_dict["event_id"])
            )
        )
        return is_success
