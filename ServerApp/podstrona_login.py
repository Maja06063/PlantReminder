from flask import render_template

def generate_one_card(plant) -> str:

    card = """
        <div class="card">
            <center>
                <h2 class="no-bold-header">%s</h2>
                <span style="display: block";> Następne podlewanie: </span>
                <span style="display: block";> Następne nawożenie: </span>
                <span style="display: block";> Następne wydarzenie: </span>
            </center>
        </div>
        """ % plant[3]

    return card

def generate_plants_cards(plants) -> str:

    cards = ""
    for plant in plants:
        cards += generate_one_card(plant)

    cards_script = """<script>var plant_cards = document.getElementById("plant_cards");
        plant_cards.innerHTML = `%s`;</script>""" % cards

    return cards_script

def generate_logged_page(args_dict, connection) -> str:

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Plants WHERE login = '" + args_dict["login"] + "';")
    plants = cursor.fetchall()

    print(plants)


    return render_template("podstrona_login.html") + generate_plants_cards(plants)