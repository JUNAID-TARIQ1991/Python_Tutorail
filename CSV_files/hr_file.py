import csv
with open("hr_data.csv", "w") as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(["Name", "Hire Date", "Salary", "Sick Days remaining"])
    writer.writerow(["Graham Chapman", "03/15/14", "50000.00", "10"])
    writer.writerow(["John Cleese", "06/01/15", "65000.00", "8"])
