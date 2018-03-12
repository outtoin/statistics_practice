import csv

def csv_length(data):
    length = 0
    with open(data, 'r') as f:
        reader = csv.reader(f)
        length = len(next(reader))
    return length