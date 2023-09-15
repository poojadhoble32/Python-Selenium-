import xlsxwriter


def writeexcel():
    data = [['Name', 'Branch', 'Year', 'CGPA'],
            ['Nikhil', 'COE', '2', '9.0'],
            ['Sanchit', 'COE', '2', '9.1'],
            ['Aditya', 'IT', '2', '9.3'],
            ['Sagar', 'SE', '1', '9.5'],
            ['Prateek', 'MCE', '3', '7.8'],
            ['Sahil', 'EP', '2', '9.1']]

    print(len(data))

    wb = xlsxwriter.Workbook('Marvellouswrite.xlsx')

    worksheet = wb.add_worksheet()

    for row, x in enumerate(data):
        print(row, x)
        for col, y in enumerate(x):
            print(col, y)
            worksheet.write(row, col, y)

    wb.close()

if __name__ == '__main__':
    writeexcel()
