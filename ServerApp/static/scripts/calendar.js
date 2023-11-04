let browsing_date = new Date(),
today = new Date();
const months = ["Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec", "Lipiec",
              "Sierpień", "Wrzesień", "Październik", "Listopad", "Grudzień"];
let table_fields = document.querySelectorAll("#calendar tbody td");

let user_events = {};

function prev_month(){
    browsing_date = new Date(browsing_date.getFullYear(), browsing_date.getMonth() - 1, 1);
    generate_calendar();
}
function next_month(){
    browsing_date = new Date(browsing_date.getFullYear(), browsing_date.getMonth() + 1, 1);
    generate_calendar();
}
function clear_calendar(){
    for(i=0;i<table_fields.length;i++){
        table_fields[i].innerHTML ="";
    }
}
function generate_calendar(){
    let first_date_of_month = new Date (browsing_date.getFullYear(),browsing_date.getMonth(),1);
    let last_date_of_month = new Date (browsing_date.getFullYear(),browsing_date.getMonth()+1,0);
    let first_day_of_week = first_date_of_month.getDay();
    if (first_day_of_week ==0){
        first_day_of_week=7;
    }
    // Obliczanie różnicy między datami w milisekundach
    let milisec_in_month=Math.abs(last_date_of_month - first_date_of_month);
    // Obliczanie liczby dni
    let days_in_month = Math.floor(milisec_in_month / (1000 * 60 * 60 * 24));
    clear_calendar();

    document.querySelector("#calendar_top").innerHTML = months[browsing_date.getMonth()]

    browsing_date_events = [];
    for (const i in user_events) {
        event_date = new Date(user_events[i][3]);
        if(event_date.getFullYear()==browsing_date.getFullYear()){
            if(event_date.getMonth()==browsing_date.getMonth()){
                browsing_date_events.push(user_events[i]);
            }
        }
    }

    for(i=1;i<days_in_month+2;i++) {
        table_fields[i+first_day_of_week-2].innerHTML = make_day_without_tooltip("other_days_icon", i, browsing_date.getMonth(), browsing_date.getFullYear());
        if (i == today.getDate() && today.getMonth()==browsing_date.getMonth()) {
            table_fields[i+first_day_of_week-2].innerHTML = make_day_without_tooltip("today_icon", i, browsing_date.getMonth(), browsing_date.getFullYear());
        }

        let that_day_events=[];
        for(const j in browsing_date_events){
            event_date = new Date(browsing_date_events[j][3]);
            if(event_date.getDate()==i) {
                that_day_events.push(browsing_date_events[j]);
            }
        }
        if (that_day_events.length) {
            if (i == today.getDate() && today.getMonth()==browsing_date.getMonth()){

                table_fields[i+first_day_of_week-2].innerHTML = make_tooltip_for_day(that_day_events, "event_today_icon", i, browsing_date.getMonth(), browsing_date.getFullYear());
            }
            else {
                table_fields[i+first_day_of_week-2].innerHTML = make_tooltip_for_day(that_day_events, "event_icon", i, browsing_date.getMonth(), browsing_date.getFullYear());
            }
        }
    }
}
//TODO 
//funkcja do pobierania eventów z serwera
async function get_user_events() {

    const response = await fetch("/user_events");
    user_events = await response.json();
}

function make_day_without_tooltip(css_class, day_number, month_number, year_number) {

    console.log(day_number)
    day_content = `<span class=${css_class} onclick="redirect_to_add_event(0, ${day_number},${month_number},${year_number})">${day_number}</span>`;
    return day_content;
}

function make_tooltip_for_day(events, css_class, day_number, month_number, year_number) {

    let tooltiptext = "<hr>";
    const needed_indexes = [1, 2, 4, 5];
    for(const j in events) {
    
        for (const i in needed_indexes) {
            if (events[j][needed_indexes[i]]) tooltiptext += `${events[j][needed_indexes[i]]}<br>`;
        }
        tooltiptext += `<button id="edit_plant_button" onclick="redirect_to_add_event(${events[j][0]}, ${day_number},${month_number},${year_number} )"><img class="care_icon" src="/static/img/pencil.png" alt="Edytuj"></button>
            <button id="remove_plant_button" onclick="remove_event(${events[j][0]})"><img class="care_icon" src="/static/img/false.png" alt="X"></button>`;
        tooltiptext += "<hr>";
    }

    tooltip_string = `
        <div class='tooltip'>
            <span class=${css_class} onclick="redirect_to_add_event(0, ${day_number},${month_number},${year_number})">${day_number}</span>
                <span class="tooltiptext">${tooltiptext}</span>
        </div>`

    return tooltip_string;
}

function remove_event(special_event_id) {

    const event_data = {special_event_id: special_event_id};
    if (!confirm("Czy na pewno usunąć wydarzenie?")) {
      return;
    }
  
    let fetch_options = {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(event_data)
    };
  
    fetch("/remove_event", fetch_options)
    .then(response => {
      if (response.status == 204) {
        window.location.href = "/calendar";
      }
      else alert("Nie udało się usunąć wydarzenia");
    });
}

//wybieranie daty z kalendarza
function redirect_to_add_event(event_id, day_number, month_number, year_number) {
    //document.cookie="date = "
    window.location.href=`/event_form?event_id=${event_id}&day=${day_number}&month=${month_number+1}&year=${year_number}`;
}






get_user_events();
setTimeout(generate_calendar, 100);
