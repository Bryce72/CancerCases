# The code in this file has user interactions: getting specified gender, getting specified race, and getting specified state

# Might add specified cancer aswell


# had to make this a global to access in the apps dropdown menu ):
states_dictionary = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
        }


'''
This function askes which gender they would like to see data on.

returns a string
'''
def get_gender():
    gender = input("Would you like to see data on male, female or both genders: ")
    if gender.capitalize() == 'M' or gender.capitalize() =='Male':
        gender = 'Male'
    elif gender.capitalize() == 'F' or gender.capitalize() == 'Female':
        gender = 'Female'
    elif gender.capitalize() == 'B' or gender.capitalize() == 'Both':
        return 'Male and Female'
    elif gender != 'Male' or gender != 'Female' or gender != 'Both':
        print("Please type in m for male, f for female or b for both. Or you can just type in Male, Female or Both.")
        return get_gender()
    return gender.capitalize().strip()


'''
This function will ask for the specific race that the user wants.
'''
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

#  I need to fix the range in which the number the user can input is... and i need to fix if they typed a letter so it doesnt pop up an error as it is right now.

'''
A function that will ask for specific State.
Set up a cool dictionary for gathering states: (key = abbreviation of state, value = Full state name)
Does not include Hawaii or Puerto Rico because the data provided unfortunately does not either. 
returns a string
'''
def get_state():
    state_input = input("Enter a State or the abbreviation to a State: ").strip().capitalize()
    abbreviation = state_input.upper()
    if abbreviation in states_dictionary:
        return states_dictionary[abbreviation]
    elif state_input in states_dictionary.values():
        return state_input
    else:
        print("Enter a valid State")
        return get_state()