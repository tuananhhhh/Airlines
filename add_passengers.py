import tkinter as tk
import tkinter.messagebox as messagebox
import pyperclip
from tkcalendar import DateEntry

def create_add_passengers_tab(parent):
    def submit_adult():
        first_name = adult_first_name_entry.get().strip()
        last_name = adult_last_name_entry.get().strip()
        gender = adult_gender_var.get()

        if not (first_name and last_name and gender):
            messagebox.showwarning("Missing Information", "Please enter all the required information.")
            return

        full_name = f"{last_name}/{first_name}"
        name_prefix = "MR" if gender == "MR" else "MS"

        record = f"NM1{full_name.upper()} {name_prefix}"
        adult_output_button.config(text=record)
        adult_output_button.config(state=tk.NORMAL)

    def submit_child():
        first_name = child_first_name_entry.get().strip()
        last_name = child_last_name_entry.get().strip()
        dob = child_dob_entry.get_date()
        birth_date = dob.strftime("%d%b%y").upper()

        if not (first_name and last_name and dob):
            messagebox.showwarning("Missing Information", "Please enter all the required information.")
            return

        full_name = f"{last_name}/{first_name}"
        record = f"NM1{full_name.upper()}(CHD/{birth_date})"
        child_output_button.config(text=record)
        child_output_button.config(state=tk.NORMAL)

    def copy_to_clipboard(record):
        pyperclip.copy(record)
        messagebox.showinfo("Success", "Copied to clipboard!")

    def submit_adult_infant():
        a_first_name = adult2_first_name_entry.get().strip()
        a_last_name = adult2_last_name_entry.get().strip()
        gender = adult_gender_var_2.get()

        c_first_name = infant_first_name_entry.get().strip()
        dob = infant_dob_entry.get_date()
        c_birth_date = dob.strftime("%d%b%y").upper()

        if not (a_first_name and a_last_name and gender and c_first_name and dob and c_birth_date):
            messagebox.showwarning("Missing Information", "Please enter all the required information.")
            return

        a_full_name = f"{a_last_name}/{a_first_name}"
        name_prefix = "MR" if gender == "MR" else "MS"

        record = f"NM1{a_full_name.upper()} {name_prefix}(INF/{c_first_name.upper()}/{c_birth_date})"
        adult2_output_button.config(text=record)
        adult2_output_button.config(state=tk.NORMAL)

    def submit_adult_infant_2():
        a_first_name = adult3_first_name_entry.get().strip()
        a_last_name = adult3_last_name_entry.get().strip()
        gender = adult_gender_var_3.get()

        c_first_name = infant_first_name_entry_3.get().strip()
        c_last_name = infant_last_name_entry_3.get().strip()
        dob = infant_dob_entry_3.get_date()
        c_birth_date = dob.strftime("%d%b%y").upper()

        if not (a_first_name and a_last_name and gender and c_first_name and c_last_name and dob and c_birth_date):
            messagebox.showwarning("Missing Information", "Please enter all the required information.")
            return

        a_full_name = f"{a_last_name}/{a_first_name}"
        name_prefix = "MR" if gender == "MR" else "MS"

        record = f"NM1{a_full_name.upper()} {name_prefix}(INF/{c_last_name.upper()}/{c_first_name.upper()}/{c_birth_date})"
        adult3_output_button.config(text=record)
        adult3_output_button.config(state=tk.NORMAL)

    # Create the widgets for the "Add Passengers" tab
    title_label = tk.Label(parent, text="Passenger Adult Name", font=("Arial", 8, "bold"))
    title_label.grid(row=0, column=0, padx=5, pady=10, sticky="w")

    adult_first_name_label = tk.Label(parent, text="Adult First Name:", anchor="w")
    adult_first_name_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

    adult_first_name_entry = tk.Entry(parent)
    adult_first_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    adult_last_name_label = tk.Label(parent, text="Adult Last Name:", anchor="w")
    adult_last_name_label.grid(row=1, column=2, padx=5, pady=5, sticky="w")

    adult_last_name_entry = tk.Entry(parent)
    adult_last_name_entry.grid(row=1, column=3, padx=5, pady=5, sticky="w")

    adult_gender_label = tk.Label(parent, text="Adult Gender:", anchor="w")
    adult_gender_label.grid(row=1, column=4, padx=5, pady=5, sticky="w")

    adult_gender_var = tk.StringVar()
    adult_gender_var.set("MR")

    adult_gender_radio_male = tk.Radiobutton(parent, text="MR", variable=adult_gender_var, value="MR", anchor="w")
    adult_gender_radio_male.grid(row=1, column=5, padx=5, pady=5, sticky="w")

    adult_gender_radio_female = tk.Radiobutton(parent, text="MS", variable=adult_gender_var, value="MS", anchor="w")
    adult_gender_radio_female.grid(row=1, column=6, padx=5, pady=5, sticky="w")

    submit_adult_button = tk.Button(parent, text="Submit Adult", command=submit_adult, anchor="w")
    submit_adult_button.grid(row=1, column=7, padx=5, pady=10, sticky="w")

    adult_output_button = tk.Button(parent, text="Adult Output", state=tk.DISABLED,
                                    command=lambda: copy_to_clipboard(adult_output_button.cget("text")))
    adult_output_button.grid(row=1, column=8, padx=5, pady=10, sticky="w")

    child_first_name_label = tk.Label(parent, text="Child Name, with date of birth:", font=("Arial", 8, "bold"), anchor="w")
    child_first_name_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

    child_first_name_label = tk.Label(parent, text="Child First Name:", anchor="w")
    child_first_name_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")

    child_first_name_entry = tk.Entry(parent)
    child_first_name_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")

    child_last_name_label = tk.Label(parent, text="Child Last Name:", anchor="w")
    child_last_name_label.grid(row=3, column=2, padx=5, pady=5, sticky="w")

    child_last_name_entry = tk.Entry(parent)
    child_last_name_entry.grid(row=3, column=3, padx=5, pady=5, sticky="w")

    child_dob_label = tk.Label(parent, text="Date of Birth:", anchor="w")
    child_dob_label.grid(row=3, column=4, padx=5, pady=5, sticky="w")

    child_dob_entry = DateEntry(parent)
    child_dob_entry.grid(row=3, column=5, padx=5, pady=5, sticky="w")

    submit_child_button = tk.Button(parent, text="Submit Child", command=submit_child, anchor="w")
    submit_child_button.grid(row=3, column=7, padx=5, pady=10, sticky="w")

    child_output_button = tk.Button(parent, text="Child Output", state=tk.DISABLED,
                                    command=lambda: copy_to_clipboard(child_output_button.cget("text")))
    child_output_button.grid(row=3, column=8, padx=5, pady=10, sticky="w")

    adult_infant_name_label = tk.Label(parent, text="Adult and Infant same surname:", font=("Arial", 8, "bold"), anchor="w")
    adult_infant_name_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")

    adult_first_name_label = tk.Label(parent, text="Adult First Name:", anchor="w")
    adult_first_name_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")

    adult2_first_name_entry = tk.Entry(parent)
    adult2_first_name_entry.grid(row=5, column=1, padx=5, pady=5, sticky="w")

    adult_last_name_label = tk.Label(parent, text="Adult Last Name:", anchor="w")
    adult_last_name_label.grid(row=5, column=2, padx=5, pady=5, sticky="w")

    adult2_last_name_entry = tk.Entry(parent)
    adult2_last_name_entry.grid(row=5, column=3, padx=5, pady=5, sticky="w")

    adult_gender_label = tk.Label(parent, text="Adult Gender:", anchor="w")
    adult_gender_label.grid(row=5, column=4, padx=5, pady=5, sticky="w")

    adult_gender_var_2 = tk.StringVar()
    adult_gender_var_2.set("MR")

    adult_gender_radio_male = tk.Radiobutton(parent, text="MR", variable=adult_gender_var_2, value="MR")
    adult_gender_radio_male.grid(row=5, column=5, padx=5, pady=5, sticky="w")

    adult_gender_radio_female = tk.Radiobutton(parent, text="MS", variable=adult_gender_var_2, value="MS")
    adult_gender_radio_female.grid(row=5, column=6, padx=5, pady=5, sticky="w")

    submit_adult_button = tk.Button(parent, text="Submit Adult", command=submit_adult_infant)
    submit_adult_button.grid(row=5, column=7, padx=5, pady=10, sticky="w")

    adult2_output_button = tk.Button(parent, text="Adult Output", state=tk.DISABLED,
                                     command=lambda: copy_to_clipboard(adult2_output_button.cget("text")))
    adult2_output_button.grid(row=5, column=8, padx=5, pady=10, sticky="w")

    child_first_name_label = tk.Label(parent, text="Child First Name:")
    child_first_name_label.grid(row=6, column=0, padx=5, pady=5, sticky="w")

    infant_first_name_entry = tk.Entry(parent)
    infant_first_name_entry.grid(row=6, column=1, padx=5, pady=5, sticky="w")

    child_dob_label = tk.Label(parent, text="Date of Birth:")
    child_dob_label.grid(row=6, column=4, padx=5, pady=5, sticky="w")

    infant_dob_entry = DateEntry(parent)
    infant_dob_entry.grid(row=6, column=5, padx=5, pady=5, sticky="w")

    adult_infant_name_label = tk.Label(parent, text="Adult and Infant different surname:", font=("Arial", 8, "bold"))
    adult_infant_name_label.grid(row=7, column=0, padx=5, pady=5, sticky="w")

    adult_first_name_label = tk.Label(parent, text="Adult First Name:")
    adult_first_name_label.grid(row=8, column=0, padx=5, pady=5, sticky="w")

    adult3_first_name_entry = tk.Entry(parent)
    adult3_first_name_entry.grid(row=8, column=1, padx=5, pady=5, sticky="w")

    adult_last_name_label = tk.Label(parent, text="Adult Last Name:")
    adult_last_name_label.grid(row=8, column=2, padx=5, pady=5, sticky="w")

    adult3_last_name_entry = tk.Entry(parent)
    adult3_last_name_entry.grid(row=8, column=3, padx=5, pady=5, sticky="w")

    adult_gender_label = tk.Label(parent, text="Adult Gender:")
    adult_gender_label.grid(row=8, column=4, padx=5, pady=5, sticky="w")

    adult_gender_var_3 = tk.StringVar()
    adult_gender_var_3.set("MR")

    adult_gender_radio_male = tk.Radiobutton(parent, text="MR", variable=adult_gender_var_3, value="MR")
    adult_gender_radio_male.grid(row=8, column=5, padx=5, pady=5)

    adult_gender_radio_female = tk.Radiobutton(parent, text="MS", variable=adult_gender_var_3, value="MS")
    adult_gender_radio_female.grid(row=8, column=6, padx=5, pady=5)

    submit_adult_button = tk.Button(parent, text="Submit Adult", command=submit_adult_infant_2)
    submit_adult_button.grid(row=8, column=7, padx=5, pady=10, sticky="w")

    adult3_output_button = tk.Button(parent, text="Adult Output", state=tk.DISABLED,
                                     command=lambda: copy_to_clipboard(adult3_output_button.cget("text")))
    adult3_output_button.grid(row=8, column=8, padx=5, pady=10, sticky="w")

    child_first_name_label = tk.Label(parent, text="Child First Name:", anchor="w")
    child_first_name_label.grid(row=9, column=0, padx=5, pady=5, sticky="w")

    infant_first_name_entry_3 = tk.Entry(parent)
    infant_first_name_entry_3.grid(row=9, column=1, padx=5, pady=5)

    child_last_name_label = tk.Label(parent, text="Child Last Name:", anchor="w")
    child_last_name_label.grid(row=9, column=2, padx=5, pady=5, sticky="w")

    infant_last_name_entry_3 = tk.Entry(parent)
    infant_last_name_entry_3.grid(row=9, column=3, padx=5, pady=5, sticky="w")

    child_dob_label = tk.Label(parent, text="Date of Birth:", anchor="w")
    child_dob_label.grid(row=9, column=4, padx=5, pady=5, sticky="w")

    infant_dob_entry_3 = DateEntry(parent)
    infant_dob_entry_3.grid(row=9, column=5, padx=5, pady=5, sticky="w")
