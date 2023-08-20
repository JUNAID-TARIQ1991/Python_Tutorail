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
    reader = csv.DictReader(File, delimiter=",")
    line_count = 0
    for row in reader:
        if line_count == 0:
            print(f'Columns names are: {", ".join(row)}')

        print(
            f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["Birth month"]}.')
        line_count += 1

    print(f'Processed {line_count} lines.')
