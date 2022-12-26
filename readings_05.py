
# Reading a CSV file using import sys and import CSV
import sys
import csv


def main():
    script = sys.argv[0]
    filename = sys.argv[1]
    date = sys.argv[2]

    with open(filename) as fh:
        rd = csv.reader(fh,
            delimiter=',',

        )

        for row in rd:
            y = row[3]
            #print(f'\t{row[1]}, {row[2]}, {row[3]}, {row[5]}.')
            if row[3] == y and date >= row[4]:
                print(f'\t{row[1]}, {row[2]}, {row[3]},{row[4]} ,{row[5]}.')
            else:
                print('Date is greater than the Vesting date')



if __name__ == '__main__':
   main()


#and date < row[4]:
