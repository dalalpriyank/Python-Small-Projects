import csv

with open('textfile.txt', 'r') as f:
    with open('mycsv.csv', 'w', newline="") as f2:
        thewriter = csv.writer(f2)
        for line in f:
            # Next line you'll add text you need to find from
            if "The operation on mailbox " in line:
                start_pt = line.find("\"")
                end_pt = line.find("\"", start_pt + 1)  # add one to skip the opening "
                quote = line[start_pt + 1: end_pt]
                print(quote)
                thewriter.writerow([quote])