import os

from Tire import Tire
import csv

class Exporter:
    def __init__(self, file_path):
        self.file_path = file_path
        file_exists = os.path.isfile(file_path)
        self.file = open(file_path, "a")
        if file_exists:
            print("File already exists, appending data.")
            self.close_file()
        else:
            writer = csv.writer(self.file)
            writer.writerow(Tire.headers())
            self.close_file()

    def open_file(self, read_mode='a'):
        self.file = open(self.file.name, read_mode, encoding='utf-8')

    def close_file(self):
        if self.file:
            self.file.close()

    def export_csv_line(self, tire):
        self.open_file('a')
        writer = csv.writer(self.file)
        writer.writerow(tire.__iter__())
        self.close_file()

    def read_csv_lines(self):
        self.open_file(read_mode='r')
        self.file.seek(0)
        lines = self.file.readlines()
        lines = lines[1:]
        self.close_file()

        cleaned_lines = []
        for line in lines:
            cleaned_lines.append(line.strip())

        tires = []
        for line in cleaned_lines:
            tire = Tire()
            tire.load_from_csv_line(line)
            tires.append(tire)

        return tires