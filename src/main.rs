use std::fs;
use std::env;
use std::str::Lines;
use std::iter::Iterator;
use std::collections::HashSet;
use std::collections::HashMap;

pub struct Agency {
    id: String,
    name: String,
    url: String,
    timezone: String,
    lang: String,
    phone: String,
    fare_url: String
}


pub struct CalendarDates {
    service_id: String,
    date: String,
    exception_type: String
}

pub struct Calendar {
    service_id: String,
    monday: String,
    tuesday: String,
    wednesday: String,
    thursday: String,
    friday: String,
    saturday: String,
    sunday: String,
    start_date: String,
    end_date: String
}

fn main() {
    // Initialize a list of supported cities.
    let mut cities = HashSet::new();
    cities.insert("San_antonio".to_string());
    cities.insert("Pittsburgh".to_string());

    // Describing the supported files in each city.
    // Pittsburgh
    let mut pittsburgh = HashSet::new();
    pittsburgh.insert("agency".to_string());
    pittsburgh.insert("calendar_dates".to_string());
    pittsburgh.insert("calendar".to_string());
    pittsburgh.insert("fare_attributes".to_string());
    pittsburgh.insert("feed_info".to_string());
    pittsburgh.insert("frequencies".to_string());
    pittsburgh.insert("routes".to_string());
    pittsburgh.insert("shapes".to_string());
    pittsburgh.insert("stop_times".to_string());
    pittsburgh.insert("stops".to_string());
    pittsburgh.insert("transfers".to_string());
    pittsburgh.insert("trips".to_string());

    // San Antonio
    let mut san_antonio = HashSet::new();
    san_antonio.insert("agency".to_string());
    san_antonio.insert("calendar_dates".to_string());
    san_antonio.insert("calendar".to_string());
    san_antonio.insert("feed_info".to_string());
    san_antonio.insert("routes".to_string());
    san_antonio.insert("shapes".to_string());
    san_antonio.insert("stop_times".to_string());
    san_antonio.insert("stops".to_string());
    san_antonio.insert("transfers".to_string());
    san_antonio.insert("trips".to_string());

    // Associate each city with a HashSet containing its provided GTFS static files.
    let mut static_files_by_city = HashMap::new();

    static_files_by_city.insert("San_antonio", san_antonio);
    static_files_by_city.insert("Pittsburgh", pittsburgh);

    let args: Vec<String> = env::args().collect();
    let city_name = &args[1];
    let file_name = &args[2];

    let file_path = "static/san_antonio/agency.txt";
    println!("In file {}", file_path);
    let file_contents = fs::read_to_string(file_path)
        .expect("File read should be successful.");

    let mut line_iterator: Lines = file_contents.lines();

    let header = line_iterator.nth(0);
    dbg!(header);



    for line in line_iterator {
        line_splitter(line, file_name);
    }
}

fn line_splitter(line: &str, file_name: &str) {
    let term = line.split(",");
    let variable: Vec<&str> = term.collect();

    if file_name == "agency" {
        agency_assignments(variable);
    } else if file_name == "calendar_dates" {
        calendar_dates_assignments(variable);
    } else if file_name == "calendar" {

    }
}

fn agency_assignments(variable: Vec<&str>) {
    let agency_id = variable[0].to_string();
    let agency_name = variable[1].to_string();
    let agency_url = variable[2].to_string();
    let agency_timezone = variable[3].to_string();
    let agency_lang = variable[4].to_string();
    let agency_phone = variable[5].to_string();
    let agency_fare_url = variable[6].to_string();
}

fn calendar_dates_assignments(variable: Vec<&str>) {
    let service_id = variable[0].to_string();
    let date = variable[1].to_string();
    let exception_type = variable[2].to_string();
}

