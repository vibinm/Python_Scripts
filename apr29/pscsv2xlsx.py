import pyexcel
import csv


def csv2xlsx(csv_file, spreadsheet_file):
    content = [row for row in csv.reader(open(csv_file), delimiter=':')]
    pyexcel.save_as(dest_file_name=spreadsheet_file, array=content)


csv2xlsx('passwd.txt', 'passwd.xlsx')