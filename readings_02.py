"""
import sys
import csv

def main():
    script = sys.argv[0]
    csv_file = sys.argv[1]
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row)

if __name__ == '__main__':
   main()
"""
# Reading a CSV file using import sys and import CSV
import sys
import csv

"""
if len(sys.argv) != 2:
    sys.stderr.write("Usage: {} FILENAME\n".format(sys.argv[0]))
    exit()
"""

def main():
    script = sys.argv[0]
    filename = sys.argv[1]
    target_date = sys.argv[2]
    #count = 0
    #result = []
    #seen = set()
    with open(filename) as fh:
        rd = csv.reader(fh,
            delimiter=',',
            #strict=True,
        )

        for row in rd:
            print(f'\t{row[1]}, {row[2]}, {row[3]}, {row[5]}.')
            #print(row)
            #if row not in rd:
                #result.append(row)
                #print('appended', result)
                #print(row)



if __name__ == '__main__':
   main()
