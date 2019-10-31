import csv


def clearRow(numRows):

    user_input = input("What is this row ")
    print(user_input)
    # if user_input
    # if numRows > 0:


def clearColumn():
    print("test")

def row_by_row(data):
    rows = len(data)
    columns = len(data[0])
    numRows = int(len(data))
    numColumns = int(len(data[0]))

    print('rows: {}  columns: {}'.format(rows, columns))

def safedata():
    k = 0
    
    try:
        savedData = open(k+"out.csv", "w", newline="")
        writer = csv.writer(savedData)
        writer.writerows(data)
    except FileNotFoundError:
        k += 1
        newSavedData = open(k+"out.csv", "w", newline="")

def column_by_column():
    print("joe")

if __name__ == '__main__':
    data = [['input1', 'input2'],
            ['input3', 'input4'],
            ['input5', 'input6']]
    numRows = int(len(data))
    numColumns = int(len(data[0]))
    safedata()
    clearRow(numRows)
    row_by_row(data)


    # myList =
    # d.write()
    # d.close()
    # column_by_column(data)
    # all_data(data)
    # terminal_prompt(data)
