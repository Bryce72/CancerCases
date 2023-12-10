# Final Project Report

* Student Name: Bryce Dunlap
* Github Username: Bryce72
* Semester: Fall 2023
* Course: CS5001




## Project overview. The incentive.

    This project takes a text file provided by cdc.gov that has data on cancer. Since the data provided by the cdc is somewhere around a million lines in a format only a goblin could
    fully read all million of, it gave me the idea to make a basic functioning gui to "visualize" that data. I chose this project for a few reasons, the most important one is my desire to
    one day become involved in cancer research and the other reasons were for challenging myself. This was alot of data to look through and required a few "tricks" I would never had done before. One of the "tricks" was, I needed to create a dictionary of all the states where data was available, some in the US were not, like Hawaii. So, I had to loop through all the States,
    not repeating and printing them out so I could structure my dictionary on the States correctly.


## Basic key features.

    I'd say the biggest key feature to this project is the GUI. Once that was incorperated into the project it became much cooler. This is something I had never done before and I am sure there are different packages I could have used besides tkinter that would have made the GUI neater but this was the one I went with for simplicity sake. This turned the project into what felt like a form of art. I felt as though I could build anything onto this app, I have so much data and the options are limitless! You will even notice I changed the little icon and title for the gui when it is open, and made my own error pop up (enter something invalid, like an empty box when choosing a state)!

## Guide to running the project.

    You will need 5 files within the same directory for this program to run, the files are: [BYAREA_modified.txt, favicon.ico, functions.py, input_actions.py, main.py]. To run the program you will need to go into your terminal and navigate to the file directory where all these are stored and type: py main.py

    If you recieve an error when clicking the "Confirm Selection" box in the DROPDOWN BOX interphase, read what the error says but most importantly know the dropdown box will be hiding behind all your programs (not sure how to force it to the front WITH the error message).


## Required installments.

    Thankfully Tkinter is installed by default with python on windows, you can check this by typing: python -m tkinter       to confirm.
    If for whatever reason Tkinter is not installed just simply do: pip install tkinter


## Reviewing the code. Talking about what I thought was important.

    What really set the tone for this project was using pandas library,
```python

    data = pd.read_csv('BYAREA_modified.txt', sep='|')
```
    This created a dataframe of over 1M lines of data needed and stored it in a "tabular" fashion from the text file provided by the cdc. This enabled me to loop through the data frame using itertuples() which returns each row as a tuple, but what was esspecially neat about using this method was being able to do things like, row.COUNT to access specific columns in the row in a convinent manner which enabled me to pick and choose specific data to show. Also, note that using the sep='|' was essential to creating a usuable data fram for myself. As the text file I was using had a '|' seperating each column.

    Finding tkinter made this project much much cooler, but I quickly ran into the issue of integrating the code I had already written into the GUI. I started off writing the code to be functional only in the terminal, which is why I have things like:

    ```python
    def get_race():
    race_list = ["All Races", "Hispanic of any race", "Non-Hispanic American Indian/Alaska Native", "Non-Hispanic Asian/Pacific Islander", "Non-Hispanic Black", "Non-Hispanic White"]
    race_input = input("Please pick a specific race you would like to see data on: \n"
                 "To select ALL races, type: 1 \n"
                 "To select Hispanic of any race, type: 2 \n"
                 "To select Non-Hispanic American Indian/Alaska Native, type: 3 \n"
                 "To select Non-Hispanic Asian/Pacific Islander, type: 4\n"
                 "To select Non-Hispanic Black, type: 5\n"
                 "To select Non-Hispanic White, type: 6\n"
                 "Type selection 1-6 here:  ")
    race = int(race_input)
    if race_list[race - 1]:
        print("Test succeeded!!!!!!!!")
    else:
        print("\n\n")
        print("Please enter a valid number corresponding to specified race...\n\n\n")
        get_race()
    print("winner")
    ```

    This was made specifically for the terminal usage of the program. Hence the print messages and the input functions. However, I'd like to go over this function as the code behind it was kinda cool, it could lead to alot more creative ideas given the time. So, within the text file there were about a million lines of data, so I didn't fully know how all the races were written out, this was an issue when trying to create this function. This also follows up on why using pandas was so important. So, I used pandas 'unique()' function to find all the information on how the races were written in the text file. Like this:

    ```python
    unique = data['RACE'].unique()
    for i in unique:
        print(i)
    ```

    You wont see this code in the submission but it was important in creating some of the functions and even the dictionary of states. As the column selection was interchangable such as using ['SITE'] to get a print out of all the cancer sites (names of the cancers) within the text file in a way where it didn't print a million baggilion times and only once.

    What I do need a further understanding on is integrating my code to the GUI I made. This was a very difficult part. Ofcourse I started off with importing the files where my functions and user inputs were. But creating the functionality behind each code became a challenging task. 

    ```python
    def highest_cancer_incidence_state(self):
        self.textbox.config(state = tk.NORMAL)
        self.textbox.delete(1.0, tk.END)
        highest_cancer_incidence = functions.highest_cancer_incident_out_of_all()
        filtered_state = highest_cancer_incidence[1]
        self.textbox.insert(tk.END, f"The State in which has the highest cancer incidence rate from the years 2016-2020 is: {filtered_state}\n This is for both genders aswell as all races")
        self.textbox.config(state=tk.DISABLED)
    ```

    Here I will go line by line trying to state what each does. So, I start off with passing 'self' as a parameter in this function because it was basically the back bone of the GUI, it was the class that held the ability to use any of the methods like .textbox. The self.textbox.config(state = tk.NORMAL) line is basically having the GUI's textbox become editable, there was probably a better way to go about this but basically I had to make the textbox's state 'normal' and then disable it after the function was done using it as seen here: self.textbox.config(state=tk.DISABLED) to avoid it being editable by the user since there was no need for that. The next line where you see the textbox.delete is there to make sure the textbox displaying the information doesn't get cluttered if the user desides to click the button a million times. Then, I set a variable to the function highest_cancer_incident_out_of_all() which is imported from the file 'functions.py' to something more manageable in a single variable name. I then need to filter the variable so it is only assigned to the specific information I want to display in the row which is the state in this case, which is the 2nd element in the list, which is why I use [1] to access it. Then I will display the message formating it so I can show what is in the filtered state variable. Also, not entirely sure why I needed to use tk.END but that is what is shown in tkinters manual which was needed.


### The major challenge of the project.

    So, the biggest key feature was using pandas library and this wasn't something I knew about going into the project. At first I was like, I can just iterate through each row on my own and assign each row to a key and value for a dictionary. However, this led me down a hole with no return, there was just too many lines and it jsut got more and more confusing. That is when I came across panda data frame via: https://www.w3schools.com/python/pandas/pandas_dataframes.asp and https://www.geeksforgeeks.org/python-read-csv-using-pandas-read_csv/?ref=lbp and https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html

    The learning curve for this became much easier then what I was attempting before.


## Video and overview of the program and how to run it.

You will see text output and user inputs within the code, this is because I wrote the code to become functional within the terminal itself at first. You will also see the main function within the functions.py file being unused and noted off, this is because it was of no use when I created the GUI and actually I didn't like the fact that it would still output the text while the GUI was running, so I made it a note. If you look close enough you will also see the get_race() function not being used. This is because when implimenting the GUI things became much more complicated adding an option on the GUI could have been done but with the limited time it was rendered unimportant for when running from the GUI. You will also see a note under the function saying it does not pass for edgecase testing, which is true. If you were to run that function and typed in an 'f' for example it would return an error.

 To run the program have these files in the same directory: [BYAREA_modified.txt, favicon.ico, functions.py, input_actions.py, main.py]
    Once you have them all in the same directory, open your terminal and naviage to the directory where they are contained and type: py main.py
Example run: https://youtu.be/F4JGMmJzvro


## What could I have added?

    There is so much that I couldn't get to on this project. Just to start off, displaing data specific to certain cancers, ages, races, and so forth was something I would have loved to tackle. Also, using matplotlib to display graphs was in the works but became to much of a learning curve to where I had to scrap it and continue on with the project without it. There was truely a limitless amount of things I could have added to this project which made it so much fun. But definately implementing matplotlib for some graphs on the data will be something I will add in the future. As I will with most definately continue this project for my own satisfaction.


## Reflecting on the project. What I learned, what I want to learn and overall thoughts.

    This has been the coolest cousrse I have possibly ever taken, outside of computational biology and cancer biology classes. This was unique in a sense where I leanred a SKILL rather than memorization of a topic. Little things started to add up during this course such as using certain extentions on my vs code like the spaces checker. Finally being able to upload to a repository and knowing how to do that now! Before this course, I was getting confused on matrices and how to properly iterate through it but now aftering learning some pythong (was using c) it became much more understanding and my confidence has gone up.

    Things that I would need to learn more of is creating dictionaries and recursive functions. I tried to challenge myself with both for this project as I created a dictionary for the states and tried using what I think is a recursive function for the get_race() function when the user does not enter a correct input. However, I know these two need work, alot of it. I don't think I fully understand the power of using a dictionary which is why I found using pandas database as the solution, it seemed to do the heavy lifting for me. I am not to sure if it is common to just import all the 'hard work' but it did seem to work just fine for my project, making things convinent and time efficent.

    The most important lesson I learned from this course is that coding in itself is easy, but it needs practice and alot of it. What I mean by that is, there is a skill to learn over time when learning how to code. Things like already knowing .unique() function exists within panda are things that come with time and practice. So, in order for me to become the best 'coder' I can possibly become that means practice. Reading and watching videos doesn't go as far as actually typing in the code myself even if I am just looking at the lecture video seeing them display code on a recursive function, for me following along and physically typing out that code is what makes a huge difference in learning it. I also learned that there is practically a library for all my needs and creative desires but I know that just importing all the librarys I'd ever use wouldn't be 'good' practice unless I understand what the imported code is actually doing. 