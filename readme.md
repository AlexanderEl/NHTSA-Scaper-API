## NHTSA API

This program allows the user to retrieve vehicular information from the NHTSA database in a clean and convenient manner.

## How to use this program
Flask is necessary to run the frontend, but if that is not used (by running python3 processing.py) then no external modules are required.
All the data gathering, cleaning and processing is done in a single place to avoid needing a frontend endpoint.
processing.py is found inside of the api directory, as when when run with the flask frontend it is all part of the api package. 

## Get Manufacturers
By accessing localhost:5000/manufacturers, the first page of NHTSA manufacturerrs will be retrieved, cleaned and processed into ease to access data.

#### Get all manufacturers
Since NHTSA does not have a single access point for getting all the data that is in their collection, multiple requests must be made to obtain it all.
This however is a slow process (which can be made multithreaded in the future) as need to make hundreds of api calls in order to concatenate all their data.

Therefore accessing localhost:5000/manufacturers/all will grant the results but the process will take several minutes. 
The results will contain over 500,000 unique manufactures after processing hundreds of the api calls.

**Note:** it is not advised to call for all manufacturers as it takes a long time to make that many requests.

## Get manufacturer makes
By accessing localhost:5000/makes/'manufacturer name' this will retrieve all the makes for a specific manufacturer.
This does expect that the given manufacturer's name is correctly spelled (capitalization is not important) so the NHTSA database contains that name.

## Get vehicle info via VIN
By calling localhost:5000/'vin number' this will retrieve the make, model and year based on the VIN number.
