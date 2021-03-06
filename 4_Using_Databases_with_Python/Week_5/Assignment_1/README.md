Using the Google Geocoding API with a Database and
Visualizing data on Google Map

In this project, we are using the Google geocoding API
to clean up some user-entered geographic locations of
university names and then placing the data on a Google
Map.

You should install the SQLite browser to view and modify
the databases from:

http://sqlitebrowser.org/

The first problem to solve is that the Google geocoding
API is rate limited to 2500 requests per day.  So if you have
a lot of data you might need to stop and restart the lookup
process several times.  So we break the problem into two
phases.  

In the first phase we take our input data in the file
(where.data) and read it one line at a time, and retreive the
geocoded response and store it in a database (geodata.sqlite).
Before we use the geocoding API, we simply check to see if
we already have the data for that particular line of input.

You can re-start the process at any time by removing the file
geodata.sqlite

Run the geoload.py program.   This program will read the input
lines in where.data and for each line check to see if it is already
in the database and if we don't have the data for the location,
call the geocoding API to retrieve the data and store it in
the database.
