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

pub struct FareAttributes {
    fare_id: String,
    price: String,
    currency_type: String,
    payment_method: String,
    transfers: String,
    transfer_duration: String
}

pub struct FareRules {

}

pub struct Frequencies {

}

pub struct Routes {
    route_id: String,
    agency_id: String,
    route_short_name: String,
    route_long_name: String,
    route_desc: String,
    route_type: String,
    route_url: String,
    route_color: String,
    route_text_color: String
}

pub struct Shapes {

}

pub struct StopTimes {

}

pub struct Stops {
    stop_id: String,
    stop_code: String,
    stop_name: String,
    stop_desc: String,
    stop_lat: String,
    stop_lon: String,
    zone_id: String,
    stop_url: String,
    location_type: String,
    parent_station: String,
    stop_timezone: String,
    wheelchair_boarding: String
}

pub struct Transfers {
    from_stop_id: String,
    to_stop_id: String,
    transfer_type: String,
    min_transfer_time: String
}

pub struct Trips {
    trip_id: String,
    route_id: String,
    service_id: String,
    trip_headsign: String,
    trip_short_name: String,
    direction_id: String,
    block_id: String,
    shape_id: String,
    wheelchair_accessible: String,
    bikes_allowed: String
}
