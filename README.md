# TransitFoamer
For doing stuff with transit GTFS-RT data. 

Disclaimer: This project is not currently in a working state. 

# Version List

v0.4 (Currently WIP).
Reworking the app to stay away from API use and migrate to agency-provided GTFS-RT 
feeds. Current cities planned to have support: Pittsburgh, San Antonio.

v0.3.2 (April 25, 2024)
- Changed name of project from transit-api to TransitFoamer.

v0.3.1 (Mar 29, 2024)
- Added option to foam entire series of buses to app, have not implemented it yet. 

v0.3 (Mar 28, 2024)
- Now have a rudimentary foaming mode done. Supports up to 10 buses as CSV with no
space between entries. TODO: Clean up the displayed messages.

v0.2: (Mar 27, 2024)
- Now have route tracking done (loosely). Enter route followed by list of route(s)
to obtain all buses on a given route. 

v0.1: (Mar 26, 2024)
- Currently have bus stop tracking done. If user enters bus followed by bus stop
numbers, then result is a list of buses which arrive at bus stop. If multiple bus
stops are entered, then result includes list of buses with the stop at which they
arrive.
- Moved files to Pittsburgh directory.
- Changed file name from predictions.py to transit.py.

v0.1: (Mar 26, 2024)
- Currently have bus stop tracking done. If user enters bus followed by bus stop
numbers, then result is a list of buses which arrive at bus stop. If multiple bus
stops are entered, then result includes list of buses with the stop at which they
arrive.
- Moved files to Pittsburgh directory.
- Changed file name from predictions.py to transit.py.