import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import functions
import input_actions


class MyGUI:

    def __init__(self):

        self.root = tk.Tk()
        self.root.configure(background="light green") # make it nice and green lol
        self.root.title("Cancer Data Viewer")
        self.label = tk.Label(self.root, text="This program aims to make the data provided by the CDC more convienently accessible to read. \n The information displayed is provided by th CDC and United States Cancer Statistics (USCS):https://www.cdc.gov/cancer/uscs/dataviz/download_data.html", font=('Arial', 14))
        self.label.pack(padx = 10, pady = 10)

        self.root.iconbitmap(r'favicon.ico')    # changed itkinter stock photo.


        self.textbox = tk.Text(self.root, height=5, font=('Arial', 16))
        self.textbox.pack(padx = 10, pady = 10)
        self.textbox.config(state=tk.DISABLED)


        # This button is for the function that iterates through all the data in the text file to find the state with the highest incidence rate of cancer from 2016-2020, ALL genders, out of all cancers and all races
        self.button_highest_incidence = tk.Button(self.root, text="Click to see State with highest cancer incidence", font=('Arial', 12), command=self.highest_cancer_incidence_state)
        self.button_highest_incidence.pack(padx = 6, pady = 6)
        # same as the highest incidence but obviously gets the lowest
        self.button_highest_incidence = tk.Button(self.root, text="Click to see State with lowest cancer incidence", font=('Arial', 12), command=self.lowest_cancer_incidence_state)
        self.button_highest_incidence.pack(padx = 6, pady = 6)


        # this is the tough one that opens a whole new interphase
        self.button_highest_incidence = tk.Button(self.root, text="Click to here to choose a State and see the most prevalent cancer in the State", font=('Arial', 12), command=self.open_state_selection_window)
        self.button_highest_incidence.pack(padx = 6, pady = 6)


        # Simple button to quit the program
        self.quit_button = tk.Button(self.root, text='Quit', font=('Arial', 18), command =self.root.destroy)
        self.quit_button.pack(padx = 10, pady = 10)

        self.root.mainloop()


# Simple function that iterates through all the data to gather the state that has the highest incidence rate of cancer cases for the years 2016-2020
    def highest_cancer_incidence_state(self):
        self.textbox.config(state = tk.NORMAL)
        self.textbox.delete(1.0, tk.END)
        highest_cancer_incidence = functions.highest_cancer_incident_out_of_all()
        filtered_state = highest_cancer_incidence[1]
        self.textbox.insert(tk.END, f"The State in which has the highest cancer incidence rate from the years 2016-2020 is: {filtered_state}\n This is for both genders aswell as all races")
        self.textbox.config(state=tk.DISABLED)


# Same as the highest cancer incidence function except this will show the state that has the lowest cancer incidence.
    def lowest_cancer_incidence_state(self):
        self.textbox.config(state = tk.NORMAL)
        self.textbox.delete(1.0, tk.END)
        lowest_cancer_incidence = functions.lowest_cancer_incident_out_of_all()
        filtered_output = lowest_cancer_incidence[1]
        self.textbox.insert(tk.END, f"The State in which has the lowest cancer incidence rate from the years 2016-2020 is: {filtered_output}\n This is for both genders aswell as all races")
        self.textbox.config(state=tk.DISABLED)





# function to open the new interphase button
    def open_state_selection_window(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.geometry("500x250")
        self.new_window.title("Select a State and Gender: DROPDOWN BOX")

        # gota make a drop down box for the gender selection...this ended up being an absolute pain since I coded this without GUI in mind and didnt have the genders stored in a dictionary like the states were
        self.gender_label = tk.Label(self.new_window, text= "Select Gender: ", font= ('Arial', 12))
        self.gender_label.pack(padx=5, pady=5)
        gender_options = ["Male", "Female", "Male and Female"]
        self.gender_var = tk.StringVar()
        self.gender_dropdown = ttk.Combobox(self.new_window, textvariable= self.gender_var, values=gender_options)
        self.gender_dropdown.pack(padx = 5, pady = 5)

        # making a drop down menu with the dictionary I made in input_actions.py
        self.gender_label = tk.Label(self.new_window, text= "Select State: ", font= ('Arial', 12))
        self.gender_label.pack(padx = 5, pady = 5)
        states = list(input_actions.states_dictionary.values())
        self.state_var = tk.StringVar()
        self.state_dropdown = ttk.Combobox(self.new_window, textvariable = self.state_var, values = states)
        self.state_dropdown.pack(padx = 5,pady = 5)
        self.confirm_button = tk.Button(self.new_window, text = "Confirm Selection", command=self.state_gender_selected)
        self.confirm_button.pack(padx = 5, pady = 5)


    def state_gender_selected(self):
        selected_state = self.state_var.get()
        selected_gender = self.gender_var.get()

        # Learned fast that this was error prone without this implemented
        if not selected_state or selected_state not in input_actions.states_dictionary.values():
            messagebox.showerror("Selection ERROR", "Just make life easier and use the drop down box please.")
            return
        if not selected_gender or selected_gender not in ["Male", "Female", "Male and Female"]:
            messagebox.showerror("Selection ERROR", "Just make life easier and use the drop down box please.")
            return
        self.new_window.destroy()
        self.most_common_cancer_by_state_by_gender(selected_state, selected_gender)


    def most_common_cancer_by_state_by_gender(self, state, gender):
        self.textbox.config(state = tk.NORMAL)
        self.textbox.delete(1.0, tk.END)
        result = functions.most_common_cancer_per_state(state, gender)
        self.textbox.insert(tk.END, (f"The most prevalent cancer in {state} for {gender}'s is {result[7]} cancer.\n"))
        # self.textbox.insert(tk.END, f"Result: {result}")
        self.textbox.config(state = tk.DISABLED)

MyGUI()