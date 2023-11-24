import pandas as pd


df = pd.read_csv('BYAREA_modified.txt', sep='|')
print("Columns: ", df.columns)
for row in df.itertuples():
    if "Florida" in row:
        if 'Leukemias' in row:
            if 'Non-Hispanic White' in row:
                if 'Mortality' in row:
                    if '1999' in row:
                        print(row)
                    