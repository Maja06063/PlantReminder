function go_to_main_page() {
  window.location.href="/my_plants";
}

function download_species_data() {
  const species_id = document.querySelector("#species").value;
  const url = "/get_species_data?species_id="+species_id;
  fetch(url)
  .then(response => {
    return response.json();
  })
  .then(data => {
    document.querySelector("#watering_period").value = data["watering"];
    document.querySelector("#fertiliz_period").value = data["fertilization"];
  });
}

function send_plant_to_backend() {
  const plant_name = document.querySelector("#plant_name").value;
  const species = document.querySelector("#species").value;
  const watering_period = document.querySelector("#watering_period").value;
  const fertiliz_period = document.querySelector("#fertiliz_period").value;
  const plant_description = document.querySelector("#plant_description").value;
  const last_watering = document.querySelector("#last_watering").value;
  const last_fertiliz = document.querySelector("#last_fertiliz").value;
  
  const plant_data = {
    plant_name: plant_name,
    species: species,
    watering_period: watering_period,
    fertiliz_period: fertiliz_period,
    plant_description: plant_description,
    last_watering: last_watering,
    last_fertiliz: last_fertiliz
  };

  let fetch_options = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(plant_data)
  };

  fetch("/add_new_plant", fetch_options)
  .then(response => {
    if (response.status == 201) {
      alert("Roślina dodana");
      window.location.href = "/my_plants";
    }
    else alert("Nie udało się dodać rośliny");
  });
}

function click_checkbox(){
  const default_checkbox=document.querySelector("#default_checkbox");
  if (default_checkbox.checked){
      document.querySelector("#watering_period").disabled = true;
      document.querySelector("#fertiliz_period").disabled = true;
  }
  else{
      document.querySelector("#watering_period").disabled = false;
      document.querySelector("#fertiliz_period").disabled = false;
  }
}

var today = new Date().toISOString().split('T')[0];
document.querySelector("#last_watering").value = today;
document.querySelector("#last_fertiliz").value = today;