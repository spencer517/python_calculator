import csv
from pathlib import Path

class CsvReader:

    def __init__(self, file):
        self.data = []
        rel = Path(file)
        abs = rel.absolute()
        with open(abs) as txt:
            csv_txt = csv.DictReader(txt, delimiter=',')
            for row in csv_txt:
                self.data.append(row)
        pass