let browsing_date = new Date();
const months = ["Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec", "Lipiec",
              "Sierpień", "Wrzesień", "Październik", "Listopad", "Grudzień"];
let table_fields = document.querySelectorAll("#calendar tbody td");

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
    clear_calendar()
    document.querySelector("#calendar_top").innerHTML = months[browsing_date.getMonth()]
    for(i=1;i<days_in_month+2;i++){
        table_fields[i+first_day_of_week-2].innerHTML = i;
    }
}
generate_calendar();
