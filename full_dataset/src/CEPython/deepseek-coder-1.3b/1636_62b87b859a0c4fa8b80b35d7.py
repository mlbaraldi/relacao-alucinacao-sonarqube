import csv


def to_csv(self, separator=",", header=None):
    with open('output.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=separator)
        if header is not None:
            writer.writerow(header)
        for point in self.points:
            writer.writerow([str(coord) for coord in point])
