import csv


def load_csv(csvpath):

    with open(csvpath, 'r') as csvfile:
        data = []

        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)  # Skip the CSV header

        for row in csvreader:  # Read the CSV data
            data.append(row)
        return data


def save_csv(csvpath, data, header=None):

    with open(csvpath, 'w', newline="") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')

        if header:
            csvwriter.writerow(header)
        csvwriter.writerow(data)
