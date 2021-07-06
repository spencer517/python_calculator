import csv

class CsvReader:

    def __init__(self, file):
        self.data = []
        with open(file) as txt:
            csv_txt = csv.DictReader(txt, delimiter=',')
            for row in csv_txt:
                self.data.append(row)
        pass