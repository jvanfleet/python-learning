import csv

with open('csv_names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # for line in csv_reader:
    #     print(line['email'])

    # next(csv_reader)  #skips over first line

    # with open('csv_new_names.csv', 'w') as new_file:
    #     csv_writer = csv.writer(new_file, delimiter = '\t') #\t = escaped tab

    #     for line in csv_reader:
    #         csv_writer.writerow(line)

    with open('csv_new_names.csv', 'w', newline='') as new_file:
        fieldnames = ['first_name', 'last_name']
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter = '\t')

        csv_writer.writeheader()

        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)
