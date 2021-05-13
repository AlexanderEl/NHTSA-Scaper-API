import requests
import json


def error_log_nhtsa_request(e):
    print("Something went wrong with NHTSA request")
    print(e)
    return json.dumps("Failed NHTSA request")


def get_list_of_manufacturers(find_all=False):
    all_manufacturers_link = "https://vpic.nhtsa.dot.gov/api/vehicles/getallmanufacturers?format=json"

    def get_raw_data(get_all=False):
        if get_all:
            index = 1
            all_data = []
            while True:
                link = f"{all_manufacturers_link}&page={index}"
                try:
                    data = requests.get(link).json()
                except requests.exceptions.RequestException as e:
                    error_log_nhtsa_request(e)

                print(index)
                if data["Count"] == 0:
                    break
                else:
                    all_data.extend(data["Results"])
                index += 1
            return all_data
        else:
            try:
                return requests.get(all_manufacturers_link).json()["Results"]
            except requests.exceptions.RequestException as e:
                return error_log_nhtsa_request(e)

    raw_manufacturers = get_raw_data(get_all=find_all)

    manufacturer_list = []
    for manufacturer in raw_manufacturers:
        if manufacturer["Mfr_CommonName"] is not None:
            name = manufacturer["Mfr_CommonName"]
        else:
            name = manufacturer["Mfr_Name"]
        manufacturer_list.append(name)

    return json.dumps(manufacturer_list)  # Remove duplicates


def get_all_makes_for_manufacturer(manufacturer):
    list_of_makes_link = f"https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{manufacturer}?format=json"
    try:
        raw_makes = requests.get(list_of_makes_link).json()["Results"]
    except requests.exceptions.RequestException as e:
        return error_log_nhtsa_request(e)
    return json.dumps({manufacturer: [make["Model_Name"] for make in raw_makes]})


def get_vehicle_info_from_vin(vin):
    vin_link = f"https://vpic.nhtsa.dot.gov/api/vehicles/decodevin/{vin}?format=json"
    try:
        raw_data = requests.get(vin_link).json()["Results"]
    except requests.exceptions.RequestException as e:
        return error_log_nhtsa_request(e)

    data = {}
    for contents in raw_data:
        if contents["Variable"] == "Make":          data["Make"] = contents["Value"]
        if contents["Variable"] == "Model":         data["Model"] = contents["Value"]
        if contents["Variable"] == "Model Year":    data["Year"] = contents["Value"]

    return json.dumps({vin: data})


def main():
    all_manufacturers = get_list_of_manufacturers()
    # all_manufacturers = get_list_of_manufacturers(find_all=True)  # This will take some time to complete

    all_makes = get_all_makes_for_manufacturer("Toyota")

    vehicle_data = get_vehicle_info_from_vin("3n1ab6ap7bl729215")


if __name__ == '__main__':
    main()
