Classes
=======

The files agency.py, calendar\_dates.py, gtfs\_calendar.py, routes.py, shapes.py, stop\_times.py, stops.py, transfers.py, and trips.py have special classes that take the data from the respective .txt files and make them easier to work with.

`Agency(agency_id, agency_name, agency_url, agency_timezone, agency_lang, agency_phone, agency_fare_url)`
---------------------------------------------------------------------------------------------------------

The class `Agency` contains information about the transit agency in question.

*   `Agency.id`
*   `Agency.name`
*   `Agency.url`
*   `Agency.timezone`
*   `Agency.lang`
*   `Agency.phone`
*   `Agency.fare_url`

`Dates(service_id, date, exception_type)`
-----------------------------------------

The class `Dates` contains information about the dates through which the feed provides valid information.

*   `Dates.id`
*   `Dates.date`
*   `Dates.type`

`Calendar(service_id, monday, tuesday, wednesday, thursday, friday, saturday, sunday, start_date, end_date)`
------------------------------------------------------------------------------------------------------------

`Feed(feed_publisher_name, feed_publisher_url, feed_lang, feed_start_date, feed_end_date,feed_version)`
-------------------------------------------------------------------------------------------------------

`Routes(route_id, agency_id, route_short_name, route_long_name, route_desc, route_type, route_url, route_color, route_text_color)`
----------------------------------------------------------------------------------------------------------------------------------

The class `Routes` contains information about the routes that the transit agency runs.

*   `Routes.id` returns the ID of the route.
*   `Routes.agency` returns the agency ID.
*   `Routes.short_name` returns the short name of the route, usually the route number or identifier.
*   `Routes.long_name` returns the long name of the route, usually what is seen on the transit agency's paper schedules.
*   `Routes.desc` returns a description of the route.
*   `Routes.type` returns the type of service the route runs.
*   `Routes.url` returns the route's unique URL, if provided.
*   `Routes.color` returns the route's color.
*   `Routes.text` returns the desired color of the text, if provided.

`Shapes(shape_id, shape_pt_lat, shape_pt_lon, shape_pt_sequence, shape_dist_traveled)`
--------------------------------------------------------------------------------------

`Stoptimes(trip_id, arrival_time, departure_time, stop_id, stop_sequence, stop_headsign, pickup_type, drop_off_type, shape_dist_traveled, timepoint)`
-----------------------------------------------------------------------------------------------------------------------------------------------------

`Transfer(from_stop_id, to_stop_id, transfer_type, min_transfer_time)`
----------------------------------------------------------------------