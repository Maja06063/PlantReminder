function redirect_to_add_plant(plant_id) {
  window.location.href="/plant_card?plant_id=" + plant_id;
}

function log_out() {
  // Ustaw czas wygaśnięcia ciasteczka na datę w przeszłości (np. 1 stycznia 1970 roku)
  const allCookies = document.cookie.split(';'); // Podziel ciasteczka po średniku
  for (let i = 0; i < allCookies.length; i++) {
    const cookie = allCookies[i].trim(); // Usuń ewentualne białe znaki
    console.log(cookie);
  }
  document.cookie = "login" + "=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
  window.location.href="/";
}

function remove_plant(plant_id) {

  const plant_data = {plant_id: plant_id};
  if (!confirm("Czy na pewno usunąć roślinę?")) {
    return;
  }

  let fetch_options = {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(plant_data)
  };

  fetch("/remove_plant", fetch_options)
  .then(response => {
    if (response.status == 204) {
      window.location.href = "/my_plants";
    }
    else alert("Nie udało się usunąć rośliny");
  });
}

function water_plant(plant_id) {

  const plant_data = {plant_id: plant_id, action:"water"};
  if (!confirm("Podlałeś roślinę?")) {
    return;
  }

  let fetch_options = {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(plant_data)
  };

  fetch("/update_plant", fetch_options)
  .then(response => {
    if (response.status == 201) {
      window.location.href = "/my_plants";
    }
    else alert("Nie udało się podlać rośliny");
  });
}


function fertiliz_plant(plant_id) {

  const plant_data = {plant_id: plant_id, action:"fertiliz"};
  if (!confirm("Czy checesz nawozić roślinę?")) {
    return;
  }

  let fetch_options = {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(plant_data)
  };

  fetch("/update_plant", fetch_options)
  .then(response => {
    if (response.status == 201) {
      window.location.href = "/my_plants";
    }
    else alert("Nie udało się nawozić rośliny");
  });
}