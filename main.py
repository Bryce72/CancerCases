import tkinter as tk
from tkinter import ttk
import functions


class MyGUI:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title("Cancer Data Viewer")
        self.label = tk.Label(self.root, text="This program aims to make the data provided by the CDC more convienently accessible to read. \n The information displayed is provided by th CDC and United States Cancer Statistics (USCS):https://www.cdc.gov/cancer/uscs/dataviz/download_data.html", font=('Arial', 14))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=5, font=('Arial', 16))
        self.textbox.pack(padx=10, pady=10)
        self.textbox.config(state=tk.DISABLED)


        # This button is for the function that iterates through all the data in the text file to find the state with the highest incidence rate of cancer from 2016-2020, ALL genders, out of all cancers and all races
        self.button_highest_incidence = tk.Button(self.root, text="Click to see State with highest cancer incidence", font=('Arial', 18), command=self.highest_cancer_incidence_state)
        self.button_highest_incidence.pack(padx=10, pady=10)




        # Simple button to quit the program
        self.quit_button = tk.Button(self.root, text='Quit', font=('Arial', 18), command =self.root.destroy)
        self.quit_button.pack(padx=10, pady=10)

        self.root.mainloop()


# Simple function that iterates through all the data to gather the state that has the highest incidence rate of cancer cases for the years 2016-2020
    def highest_cancer_incidence_state(self):
        self.textbox.config(state = tk.NORMAL)
        self.textbox.delete(1.0, tk.END)
        highest_cancer_incidence = functions.highest_cancer_incident_out_of_all()
        filtered_output = highest_cancer_incidence[1]
        self.textbox.insert(tk.END, f"The State in which has the highest cancer incidence rate from the years 2016-2020 is: {filtered_output}\n This is for both genders aswell as all races")
        self.textbox.config(state=tk.DISABLED)

MyGUI()