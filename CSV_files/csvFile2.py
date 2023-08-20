import csv
# write
# with open("employee_birthday.csv", "w") as Data2:
#     writer = csv.writer(Data2)
#     writer.writerow(["name", "department", "Birth month"])
#     writer.writerow(['junaid', 'Physics', "05"])
#     writer.writerow(['Zohaib', 'Physics', "07"])
#     writer.writerow(['Qudsia', 'Physics', "08"])

# read

with open("employee_birthday.csv") as File:
    reader = csv.reader(File, delimiter=",")
    line_count = 0
    for row in reader:

        if line_count == 0:
            print(f'Columns names are: {", ".join(row)}')
            line_count += 1
        else:
            print(
                f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1

    print(f'Processed {line_count} lines.')
