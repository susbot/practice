import csv
class Vesting:
    def __init__(self, filename):
        """Initialize the filename and target date"""
        self.filename = filename
        #self.target_date = target_date

    """def file(self):
        with open('filename') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1

                else:
                    print(f'\t{row[1]}, {row[2]}, {row[3]}, {row[5]}.')
                    line_count += 1
            print(f'Processed {line_count} lines.')"""


    #def date(self):
my_vest = Vesting(csv.reader(open('example.csv')))

#my_vest.file()
print(my_vest.filename)
