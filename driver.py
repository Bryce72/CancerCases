import pandas as pd


df = pd.read_csv('BYAREA_modified.txt', sep='|')

print("The information provided here is thanks to the CDC and United States Cancer Statistics (USCS):https://www.cdc.gov/cancer/uscs/dataviz/download_data.html")
print("This program aims to make the data provided by the CDC more convienently accessible to read.\n\n")


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
#def get_race():
    








'''
A function that will ask for specific State.

Set up a cool dictionary for gathering states: (key = abbreviation of state, value = Full state name)

Does not include Hawaii or Puerto Rico because the data provided unfortunately does not either. 

returns a string
'''
def get_state():
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

    state_input = input("Enter a State or the abbreviation to a State: ").strip().capitalize()
    abbreviation = state_input.upper()
    if abbreviation in states_dictionary:
        return states_dictionary[abbreviation]
    elif state_input in states_dictionary.values():
        return state_input
    else:
        print("Enter a valid State")
        return get_state()


'''
A function that will show the highest incidence rates for all cancers, all races and all states and both genders.
'''
def highest_cancer_incident_out_of_all():
    max = 0
    max_row = None
    for row in df.itertuples():
        if '~' not in str(row.COUNT) and '+' not in str(row.COUNT) and '-' not in str(row.COUNT) and 'United States (comparable to ICD-O-2)' not in str(row.AREA):
            max_count = int(row.COUNT)
            if max_count >= max:
                max = max_count
                max_row = row
    return max_row

'''
Least common cancer filtered by state and/or gender
'''



'''
Most common cancer filtered by State; State is user inputed
'''
def most_common_cancer_per_state(state, gender):
    print("Here, will show you the most prevalent cancer cases by state and gender of your choice to search.")
    max = 0
    max_row = None
    for row in df.itertuples():
        if state.title() in row:
            if gender == 'Male':
                if 'All Cancer Sites Combined' not in row and 'Male' in row:
                    if '~' not in str(row.COUNT) and '+' not in str(row.COUNT) and '-' not in str(row.COUNT) and 'United States (comparable to ICD-O-2)' not in str(row.AREA):
                        max_count = int(row.COUNT)
                        if max_count >= max:
                            max = max_count
                            max_row = row
            elif gender == 'Female':
                if 'All Cancer Sites Combined' not in row and 'Female' in row:
                    if '~' not in str(row.COUNT) and '+' not in str(row.COUNT) and '-' not in str(row.COUNT) and 'United States (comparable to ICD-O-2)' not in str(row.AREA):
                        max_count = int(row.COUNT)
                        if max_count >= max:
                            max = max_count
                            max_row = row
            elif gender == 'Male and Female':
                if 'All Cancer Sites Combined' not in row and 'Male and Female' in row:
                    if '~' not in str(row.COUNT) and '+' not in str(row.COUNT) and '-' not in str(row.COUNT) and 'United States (comparable to ICD-O-2)' not in str(row.AREA):
                        max_count = int(row.COUNT)
                        if max_count >= max:
                            max = max_count
                            max_row = row
    return max_row


def main():
    common_cancer_by_state = most_common_cancer_per_state(get_state(), get_gender())
    print(f"The most common cancer in {common_cancer_by_state[1]} for {common_cancer_by_state[6]} is {common_cancer_by_state[7]} cancers.")

main()
