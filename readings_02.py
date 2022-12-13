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
    count = 0
    with open(filename) as fh:
        rd = csv.reader(fh,
            delimiter=',',
            #strict=True,
        )

        for row in rd:
            print(row)
if __name__ == '__main__':
   main()

#print("Total: {}".format(count))
