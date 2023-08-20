
import pandas
df = pandas.read_csv('hr_data.csv')
print(df.head())
print(df.describe())


print(type(df['Hire Date'][0]))
# print(file)
# import csv
# with open("Data.csv") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)
df = pandas.read_csv('hr_data.csv', index_col="Hire Date")


df = pandas.read_csv('hr_data.csv', index_col="Name", )
