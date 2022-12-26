
# Reading a CSV file using import sys and import CSV
import sys
import csv


def main():
    script = sys.argv[0]
    filename = sys.argv[1]


    with open(filename,'r') as in_file, open('ouput.csv','w') as out_file:

        seen = set() # set for fast O(1) amortized lookup

        for line in in_file:
            if line in seen:
              continue # skip duplicate

            seen.add(line)
            out_file.write(line)
            print(line)

"""
    with open(filename) as fh:
        rd = csv.reader(fh,
            delimiter=',',

        )


        for row in rd:
            print(f'\t{row[1]}, {row[2]}, {row[3]}, {row[5]}.')
            #row_copy = set(row[:])
            #print(row_copy)
            #print('copy',f'\t{row_copy[1]}, {row_copy[2]}, {row_copy[3]}, {row_copy[5]}.')


"""
if __name__ == '__main__':
   main()
