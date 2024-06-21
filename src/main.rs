use std::fs;
use std::env;
use std::str::Lines;
use std::iter::Iterator;
use std::collections::HashSet;
use std::collections::HashMap;

pub struct Agency {
    id: &str,
    name: &str,
    url: &str,
    timezone: &str,
    lang: &str,
    phone: &str,
    fare_url: &str
}


pub struct CalendarDates {
    service_id: &str,
    date: &str,
    exception_type: &str
}

pub struct Calendar {
    service_id: &str,
    monday: &str,
    tuesday: &str,
    wednesday: &str,
    thursday: &str,
    friday: &str,
    saturday: &str,
    sunday: &str,
    start_date: &str,
    end_date: &str
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
    
    dbg!(variable);
}

fn agency_assignments(variable: Vec<&str>) {
    let agency_id = variable[0];
    let agency_name = variable[1];
    let agency_url = variable[2];
    let agency_timezone = variable[3];
    let agency_lang = variable[4];
    let agency_phone = variable[5];
    let agency_fare_url = variable[6];
}

fn calendar_dates_assignments(variable: Vec<&str>) {
    let service_id = variable[0];
    let date = variable[1];
    let exception_type = variable[2];
}

