from flask import render_template

def generate_one_card(plant,connection) -> str:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Species WHERE species_id = '" + str(plant[2])+ "';")
    species = cursor.fetchall()
    species=list(species[0])
    plant_name=species[1]
    if None in plant[4:7]:
        for i in range(4,7):
            if plant[i]==None:
                plant[i]=species[i-2]

    card = """
        <div class="card">
            <center>
                <h2 class="no-bold-header">%s</h2>
                <span style="display: block";> Następne podlewanie:%d </span>
                <span style="display: block";> Następne nawożenie:%d </span>
                <span style="display: block";> Następne wydarzenie:%d </span>
            </center>
        </div>
        """ % (plant_name,plant[4],plant[5],plant[6])

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