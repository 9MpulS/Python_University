import csv


def FindMinMax(arr):
    minimum = 99999
    maximum = -99999
    for i in arr:
        if i == None:
            continue
        if i > maximum:
            maximum = i
        if i < minimum:
            minimum = i
    return maximum, minimum


def ToFloat(string):
    try:
        return float(string)
    except ValueError:
        return None


def readerTodDist(reader):
    __csvlist = list(csvreader)
    return dict(zip(__csvlist[0], __csvlist[1]))


if __name__ == '__main__':
    filename = "UA1991-2019.csv"
    filename2 = "result.csv"
    csvdist = {}
    try:
        with open(filename, 'r') as file:
            csvreader = csv.reader(file, delimiter=",")
            csvdist = readerTodDist(csvreader)

            print("Дані в csv:")
            for data in csvdist.items():
                print(data)

        file.close()
        print()
    except FileNotFoundError:
        print("Файла не існує")

    floatList = []
    for data in csvdist.values():
        floatList.append(ToFloat(data))
    minGDP, maxGDP = FindMinMax(floatList)

    newDict = {str(list(csvdist.keys())[list(csvdist.values()).index(str(minGDP))]): minGDP,
               str(list(csvdist.keys())[list(csvdist.values()).index(str(maxGDP))]): maxGDP}

    print(f'Максимум в {list(newDict.keys())[0]}: {list(newDict.values())[0]}')
    print(f'Мінімум в {list(newDict.keys())[1]}: {list(newDict.values())[1]}')
    try:
        with open(filename2, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(newDict.keys())
            writer.writerow(newDict.values())

    except FileNotFoundError:
        print("Файла не існує")
