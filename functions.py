import pandas as pd
import input_actions


df = pd.read_csv('BYAREA_modified.txt', sep='|')


'''
A function that will show the State that has the most cancer from 2016-2020; all races of both male and female (Incidence rate) .
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
def lowest_cancer_incident_out_of_all():
    min_count = 10000
    min_row = None
    for row in df.itertuples():
        if '~' not in str(row.COUNT) and '+' not in str(row.COUNT) and '-' not in str(row.COUNT) and 'United States (comparable to ICD-O-2)' not in str(row.AREA) and 'All Cancer Sites Combined' in str(row.SITE) and 'All Races' in str(row.RACE) and '2016-2020' in str(row.YEAR) and 'Male and Female' in str(row.SEX):
            count = int(row.COUNT)
            if count < min_count:
                min_count = count
                min_row = row
    return min_row



'''
Most common cancer filtered by State; State is user inputed same with gender
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


# Maybe I can add some sorta matplot lib insertion to give a graph



#def main():

    # Get the state and gender the user wants to gather the most common cancer per state/gender.
  #  common_cancer_by_state = most_common_cancer_per_state(input_actions.get_state(), input_actions.get_gender())
 #   print(f"The most common cancer in {common_cancer_by_state[1]} for {common_cancer_by_state[6]} is {common_cancer_by_state[7]} cancers.")
    # print(highest_cancer_incident_out_of_all())

#main()
