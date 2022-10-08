
import csv


my_new_list = open('writetest.csv', 'w', newline = '')
csv_writer = csv.writer(my_new_list)
csv_writer.writerow(["test","test2"])
my_new_list.close()
