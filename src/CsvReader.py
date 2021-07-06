import csv
import pprint

def ClassFactory(class_name, dictionary):
    return type(class_name, (object,), dictionary)

class CsvReader:

    def __init__(self, file):
        self.data = []
        with open(file) as txt:
            csv_txt = csv.DictReader(txt, delimiter=',')
            for row in csv_txt:
                self.data.append(row)
        pass

    def return_data_as_objects(self, class_name):
        objects = []
        for row in self.data:
            objects.append(ClassFactory(class_name, row))
        return objects