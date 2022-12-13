import csv

with open('example.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if row[2] == row[2] and row[3] == row[3]:
            x = int(row[5]) + int(row[5])
            print(x)

        else:
            print(f'\t{row[1]}, {row[2]}, {row[3]}, {row[5]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')
