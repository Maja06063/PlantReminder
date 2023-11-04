function go_to_main_page() {
  window.location.href="/calendar";
}

function download_names_data() {
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
function get_event_data(){
  const plant_id = document.querySelector("#plant_names_species").value;
  const event_name = document.querySelector("#event_name").value;
  const event_description = document.querySelector("#event_description").value;
  
  const event_data = {
    plant_id:plant_id,
    event_name: event_name,
    event_description: event_description
  };
  return event_data;
}
function save_edited_event(){
  event_data= get_event_data();
  event_data["event_id"]=url_params.get("event_id");

  let fetch_options = {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(event_data)
  };

  fetch("/save_event", fetch_options)
  .then(response => {
    if (response.status == 201) {
      alert("Zmiany zapisane");
      window.location.href = "/calendar";
    }
    else alert("Nie udało się zapisać zmian");
  });
}

function save_new_event() {
  event_data= get_event_data();
  event_data["event_date"]=url_params.get("year")+"-"+url_params.get("month")+"-"+url_params.get("day");

  if (!event_data["event_name"]) {
    alert("Nie udało się dodać wydarzenia. Nazwa wydarzenia jest wymagana.")
    return;
  }

  let fetch_options = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(event_data)
  };

  fetch("/save_event", fetch_options)
  .then(response => {
    if (response.status == 201) {
      alert("Wydarzenie dodane");
      window.location.href = "/calendar";
    }
    else alert("Nie udało się stworzyć wydarzenia");
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

const url = window.location.search;
const url_params = new URLSearchParams (url);
if (url_params.get("event_id")==0)
{
  var today = new Date().toISOString().split('T')[0];
  document.querySelector("#last_watering").value = today;
  document.querySelector("#last_fertiliz").value = today;
}

download_species_data();
