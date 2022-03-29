import pandas as pd

input  = pd.DataFrame(
    {
        'FLT' : ['1122', '1313', '1234', '1122', '1234'],
        'DATE' : ['2022-01-15', '2022-01-16', '2022-01-17', '2022-01-15', '2022-01-17'],
        'CHG': ['CNL', 'CNL', 'DLY', 'CNL', 'DLY' ]
    }
)
print(input)

ip2 = (input.drop_duplicates(subset = ["FLT", "DATE"])).groupby(['CHG']).size()
print("**********************")

print("CNL = ", ip2.at['CNL'])
print("DLY = ", ip2.at['DLY'])