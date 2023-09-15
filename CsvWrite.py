import csv


def csvwrite():

    fields = ['Name', 'Branch', 'Year', 'CGPA']

    rows = [['Nikhil', 'COE', '2', '9.0'],
            ['Sanchit', 'COE', '2', '9.1'],
            ['Aditya', 'IT', '2', '9.3'],
            ['Sagar', 'SE', '1', '9.5'],
            ['Prateek', 'MCE', '3', '7.8'],
            ['Sahil', 'EP', '2', '9.1']]

    with open("D:\Mine\python\SeleniumProjects\DemoFiles\democsv.csv", 'w') as csvwrite:
        csvwriteobj = csv.writer(csvwrite)
        csvwriteobj.writerow(fields)
        csvwriteobj.writerows(rows)

if __name__ == "__main__":
    csvwrite()