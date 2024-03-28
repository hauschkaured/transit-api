# transit-api
For doing stuff with transit APIs.

v0.1: (Mar 27, 2024)
- Currently have bus stop tracking done. If user enters bus followed by bus stop
numbers, then result is a list of buses which arrive at bus stop. If multiple bus
stops are entered, then result includes list of buses with the stop at which they
arrive.
- Moved files to Pittsburgh directory.
- Changed file name from predictions.py to transit.py.

v0.2: (Mar 28, 2024)
- Now have route tracking done (loosely). Enter route followed by list of route(s)
to obtain all buses on a given route. 

v0.3 (Mar 29, 2024)
- Now have a rudimentary foaming mode done. Supports up to 10 buses as CSV with no
space between entries. TODO: Clean up the displayed messages.
