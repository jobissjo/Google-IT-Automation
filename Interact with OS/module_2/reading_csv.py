#!/usr/bin/env py

import csv

data_path = './data/csv_file.csv'
with open(data_path, 'r') as file:
    csv_f = csv.reader(file)
    print(csv_f)
    for row in csv_f:
        name, phone, role = row
        print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))


#################################################################################

hosts =  [["workstation.local", "192.168.25.46"],["webserver.cloud", "10.2.5.6"]]

with open('hosts.csv', 'w') as host_csv:
    writer = csv.writer(host_csv)
    writer.writerows(hosts)

################################################################################


with open('sample_data/software.csv') as software:
    reader = csv.DictReader(software)
    for row in reader:
        print(f"{row['name']} has {row['users']} users")


###############################################################################


users = [ 
    {"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"}, 
    {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"}, 
    {"name": "Charlie Grey", "username": "greyc", "department": "Development"}
    ]


keys = ["name", "username", "department"]
with open('by_department.csv', 'w') as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)



###############################################################################
custom_dialect = csv.Dialect
custom_dialect.delimiter = ";"
custom_dialect.quotechar ='"'
custom_dialect.quoting = csv.QUOTE_MINIMAL
custom_dialect.lineterminator ='\n'


with open('output.csv', 'w') as file:
    writer = csv.writer(file, dialect=custom_dialect)
    writer.writerow(['Name', 'Age', 'Location'])
    writer.writerow(['Alice', '30', 'New York'])
    writer.writerow(['Bob', '25', 'Los Angeles'])