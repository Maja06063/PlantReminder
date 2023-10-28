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
        table_fields[i+first_day_of_week-2].innerHTML ="<span class=other_days_icon>"+i+"</span>";
        if (i == today.getDate() && today.getMonth()==browsing_date.getMonth()) {
            table_fields[i+first_day_of_week-2].innerHTML ="<span class=today_icon>"+i+"</span>";
        }
        for(const j in browsing_date_events){
            event_date = new Date(browsing_date_events[j][3]);
            if(event_date.getDate()==i){
                if (i == today.getDate() && today.getMonth()==browsing_date.getMonth()){

                    table_fields[i+first_day_of_week-2].innerHTML ="<span class=event_today_icon>"+i+"</span>";
                }
                else{
                    table_fields[i+first_day_of_week-2].innerHTML = make_tooltip_for_day(i, browsing_date_events[j], "event_icon");
                }
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

function make_tooltip_for_day(day_number, event, css_class) {

    let tooltiptext = "";
    let needed_indexes = [1, 2, 4, 5];
    for (const i in needed_indexes) {
        if (event[needed_indexes[i]]) tooltiptext += `${event[needed_indexes[i]]}<br>`;
    }

    tooltip_string = `
        <div class='tooltip'>
            <span class=${css_class}>${day_number}</span>
                <span class="tooltiptext">${tooltiptext}</span>
        </div>`

    return tooltip_string;
}

get_user_events();
setTimeout(generate_calendar, 100);
