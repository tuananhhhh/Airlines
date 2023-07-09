import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
import pyperclip
from func import get_formatted_date, create_pnr, create_return_pnr
import json

def create_generate_pnr_tab(parent):
    def generate_pnr():
        departure_date = entry_departure.get_date().strftime("%d/%m/%Y")
        departure_city = entry_departure_city.get()
        arrival_city = entry_arrival_city.get()

        if departure_date and departure_city and arrival_city:
            formatted_departure_date = get_formatted_date(departure_date)
            pnr_code = create_pnr(formatted_departure_date, departure_city, arrival_city)
            departure_output_label.config(text=pnr_code)
            pyperclip.copy(pnr_code)
        else:
            departure_output_label.config(text="Please enter departure date, departure city, and arrival city.")

    def generate_return_pnr():
        return_date = entry_return.get_date().strftime("%d/%m/%Y")

        if return_date:
            formatted_return_date = get_formatted_date(return_date)
            pnr_code = create_return_pnr(formatted_return_date)
            return_output_label.config(text=pnr_code)
            pyperclip.copy(pnr_code)
        else:
            return_output_label.config(text="Please enter return date.")

    def autocomplete(event):
        text = entry_departure_city.get()
        if text:
            matches = [city for city in city_iata_codes.keys() if city.lower().startswith(text.lower())]
            entry_departure_city['values'] = matches
            if len(matches) == 1:
                entry_departure_city.set(matches[0])
                entry_departure_city.icursor(tk.END)
        else:
            entry_departure_city['values'] = list(city_iata_codes.keys())

    def autocomplete_2(event):
        text = entry_arrival_city.get()
        if text:
            matches = [city for city in city_iata_codes.keys() if city.lower().startswith(text.lower())]
            entry_arrival_city['values'] = matches
            if len(matches) == 1:
                entry_arrival_city.set(matches[0])
                entry_arrival_city.icursor(tk.END)
        else:
            entry_arrival_city['values'] = list(city_iata_codes.keys())

    def find_best_price():
        code = "FXR"
        find_best_price_label.config(text=code)
        pyperclip.copy(code)
        find_best_price_label.config(text="FXR - Copied to Clipboard")

    city_iata_codes = {}
    airlines = {}

    with open('city_iata_codes.json') as file:
        city_iata_codes = json.load(file)

    with open('airlines.json') as file:
        airlines = json.load(file)

    # Create an entry field for the departure date
    entry_departure_label = ttk.Label(parent, text="Chon ngay bay / Choose departure date (DD/MM/YYYY):", anchor="w")
    entry_departure_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    entry_departure = DateEntry(parent, date_pattern="dd/mm/yyyy", show_weeknumbers=False)
    entry_departure.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    # Create an entry field with autocomplete for the departure city
    entry_departure_city_label = ttk.Label(parent, text="Chon diem di / Choose departure city:", anchor="w")
    entry_departure_city_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    departure_city_var = tk.StringVar()
    entry_departure_city = ttk.Combobox(parent, textvariable=departure_city_var)
    entry_departure_city.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    entry_departure_city.bind('<KeyRelease>', autocomplete)

    # Create a dropdown list for the arrival city
    entry_arrival_city_label = ttk.Label(parent, text="Chon diem den / Choose arrival city:", anchor="w")
    entry_arrival_city_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
    arrival_city_var = tk.StringVar()
    entry_arrival_city = ttk.Combobox(parent, textvariable=arrival_city_var)
    entry_arrival_city.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    entry_arrival_city.bind('<KeyRelease>', autocomplete_2)

    # Create a button to generate the PNR code for the departure date
    generate_departure_button = ttk.Button(parent, text="Tao PNR / Generate Departure PNR", command=generate_pnr)
    generate_departure_button.grid(row=3, column=0, padx=5, pady=5, sticky="w")

    # Create an entry field for the return date
    entry_return_label = ttk.Label(parent, text="Chon ngay ve / Choose return date (DD/MM/YYYY):", anchor="w")
    entry_return_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
    entry_return = DateEntry(parent, date_pattern="dd/mm/yyyy", show_weeknumbers=False)
    entry_return.grid(row=4, column=1, padx=5, pady=5, sticky="w")

    # Create a button to generate the PNR code for the return date
    generate_return_button = ttk.Button(parent, text="Tao PNR / Generate Return PNR", command=generate_return_pnr)
    generate_return_button.grid(row=5, column=0, padx=5, pady=5, sticky="w")

    # Create a button to find the best price
    find_best_price_button = ttk.Button(parent, text="Tim Gia Tot Nhat / Find Best Price", command=find_best_price)
    find_best_price_button.grid(row=6, column=0, padx=5, pady=5, sticky="w")

    # Create a label to display the generated PNR code
    departure_output_label = ttk.Label(parent, text="")
    departure_output_label.grid(row=3, column=1, padx=5, pady=5, sticky="w")

    return_output_label = ttk.Label(parent, text="")
    return_output_label.grid(row=5, column=1, padx=5, pady=5, sticky="w")

    find_best_price_label = ttk.Label(parent, text="")
    find_best_price_label.grid(row=6, column=1, padx=5, pady=5, sticky="w")