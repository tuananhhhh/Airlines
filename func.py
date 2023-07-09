from datetime import datetime
import json

city_iata_codes = {}
airlines = {}

with open('city_iata_codes.json') as file:
    city_iata_codes = json.load(file)

with open('airlines.json') as file:
    airlines = json.load(file)

def get_formatted_date(date_string):
    date = datetime.strptime(date_string, "%d/%m/%Y")
    formatted_date = date.strftime("%d%b")
    return formatted_date


def create_pnr(departure_date, departure_city, arrival_city):
    airline_codes = ','.join(airlines.values())
    departure_iata_code = city_iata_codes.get(departure_city, '')
    arrival_iata_code = city_iata_codes.get(arrival_city, '')
    departure_code = f"AN{departure_date.upper()}{departure_iata_code}{arrival_iata_code}/A{airline_codes}"

    return departure_code


def create_return_pnr(return_date):
    return_code = f"ACR{return_date.upper()}"
    return return_code


