import tkinter as tk
from tkinter import ttk
from generate_pnr import create_generate_pnr_tab
from add_passengers import create_add_passengers_tab
from tickettiming import create_ticket_timing_limit_tab
from PIL import Image, ImageTk
# Create a Tkinter window
window = tk.Tk()
window.title("PNR Code Generator")

# Create a tab widget
tab_widget = ttk.Notebook(window)

# Create the "Generate PNR" tab
generate_pnr_tab = ttk.Frame(tab_widget)
tab_widget.add(generate_pnr_tab, text="Generate PNR")

# Call the function to create the content for the "Generate PNR" tab
create_generate_pnr_tab(generate_pnr_tab)

# Create the "Add Passengers" tab
add_passengers_tab = ttk.Frame(tab_widget)
tab_widget.add(add_passengers_tab, text="Add Passengers")

# Add the content for the "Add Passengers" tab
create_add_passengers_tab(add_passengers_tab)

# Create the "Ticket Timing Limit" tab
ticket_timing_limit_tab = ttk.Frame(tab_widget)
tab_widget.add(ticket_timing_limit_tab, text="Ticket Timing Limit")

# Add the content for the "Ticket Timing Limit" tab
create_ticket_timing_limit_tab(ticket_timing_limit_tab)

# Pack the tab widget
tab_widget.pack()

# Run the Tkinter event loop
window.mainloop()




