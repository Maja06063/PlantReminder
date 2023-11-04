function go_to_main_page() {
  window.location.href="/calendar";
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

const url = window.location.search;
const url_params = new URLSearchParams (url);
