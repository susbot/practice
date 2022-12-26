
# Reading a CSV file using import sys and import CSV
import sys
import csv


def main():
    script = sys.argv[0]
    filename = sys.argv[1]

    with open(filename) as fh:
        rd = csv.reader(fh,
            delimiter=',',

        )

        for row in rd:
            print(f'\t{row[1]}, {row[2]}, {row[3]}, {row[5]}.')




if __name__ == '__main__':
   main()
