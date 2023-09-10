from flask import render_template

def generate_one_card(plant,connection) -> str:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Species WHERE species_id = '" + str(plant[2])+ "';")
    species = cursor.fetchall()
    species=list(species[0])
    species_name=species[1]
    plant_name=plant[3]
    species_desc=species[5]
    if None in plant[4:7]:
        for i in range(4,7):
            if plant[i]==None:
                plant[i]=species[i-2]

    card = """
        <div class="card">
            <center>
                <h2 class="no-bold-header">%s</h2>
                <h3 class="Species-header">%s</h3>
                <span style="display: block";> Następne podlewanie:Za <strong>%d</strong> dni</span>
                <span style="display: block";> Następne nawożenie:Za <strong>%d</strong> dni</span>
                <span style="display: block";> Następne wydarzenie:Za <strong>%d</strong> dni</span>
                <p class="species-description">Opis: %s</p>
            </center>
        </div>
        """ % (species_name,plant_name,plant[4],plant[5],plant[6],species_desc)

    return card

def generate_plants_cards(plants,connection) -> str:

    cards = ""
    for plant in plants:
        cards += generate_one_card(list(plant),connection)

    cards_script = """<script>var plant_cards = document.getElementById("plant_cards");
        plant_cards.innerHTML = `%s`;</script>""" % cards

    return cards_script

def generate_logged_page(args_dict, connection) -> str:

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Plants WHERE login = '" + args_dict["login"] + "';")
    plants = cursor.fetchall()



    return render_template("podstrona_login.html") + generate_plants_cards(plants,connection)