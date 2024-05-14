# Pittsburgh

Transit vehicles have data stored in the dictionaries `busDict` and `trainDict`.
The keys of the dictionary are the fleet numbers of buses currently running. 
Each key has a corresponding dictionary which is populated by information about 
the bus in question. The following terms are used as keys of this sub-dictionary,
and their return types are listed below:
- `busId` is the **Fleet Number** of the vehicle. Returns `str`
- `vid` is the **Vehicle ID** of the vehicle. Returns `str`
- `lat` is the **Latitude** of the vehicle. Returns `str`
- `lon` is the **Longitude** of the vehicle. Returns `str`
- `hdg` is the **Heading** of the vehicle. Returns `str`
- `speed` is the **Speed** of the vehicle. Returns `str`
- `time` is the **Timestamp** associated with the vehicle data. Returns `str`
- `stopId` is the **Current Stop** of the vehicle. Returns `str`
- `currentStopSequence` is the 

- `tripId` is the **Trip** the vehicle is operating. Returns `str`
- `tripRoute` is the **Route** the vehicle is operating. Returns `str`
- `status` is the **Status** of the vehicle. Returns `str`

Vehicle trips have their trip information stored in the dictionaries `tripDict` 
and `trainTripDict`. The keys of the dictionary are the scheduled trips currently
in the GTFS-RT feed. Each key has a corresponding dictionary populated by 
information about the trip in question. The following terms are used as keys of 
this sub-dictionary, and their return types are listed below:

- `relationship` is the **Schedule Relationship** of the trip. Returns `str`
- `route` is the **Scheduled Route** of the trip. Returns `str`
- `timedata` is the **Timestamp** of the trip. Returns `str`
- `timeUpdateList` is the **List of Scheduled Stops** for the trip. Returns `list`.

## timeUpdateList

Every entry in 