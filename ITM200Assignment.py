import matplotlib.pyplot as plt
import csv
with open('Data.csv', mode = 'r') as fileCSV: # Opening the sample.csv file
    fCSV = csv.reader(fileCSV)                  # Reading the csv file
    for line in fCSV:
        print(line)                     # Printing file content line by line

with open('Data.csv', mode='r') as fileCSV:  # Opening the sample.csv file
    fCSV = csv.reader(fileCSV)
    sumsales = []
    years = ['2012', '2013', '2014','2015','2016','2017','2018','2019','2020','2021']
    for line in fCSV:
        year = line[0]
        if year in years:
            yearsales = 0
            for sales in line[1:]:
                yearsales += int(sales)
            sumsales += [yearsales]


    #print(sumsales)

    file=open('stats.txt','w')
    for sales in sumsales:
        text = str(sales) + "\n"
        file.write(text)

    x = years
    y = sumsales

    plt.figure(1)
    plt.bar(x, y)

    plt.title("Car Sales")  # Writing plot title
    plt.xlabel("Years")  # Writing x-axis label
    plt.ylabel("Sales")  # Writing y-axis label

    plt.show()

    sales2021 = 0
    sales2022 = 0
    with open('Data.csv', mode='r') as fileCSV:  # Opening the sample.csv file
        fCSV = csv.reader(fileCSV)
        gyears = ['2021','2022']
        for line in fCSV:
            year = line[0]
            if year in gyears:
                if year == '2021':
                    year2021 = line
                if year == '2022':
                    year2022 = line
        for sales in year2021[1:7]:
            sales2021 += int(sales)
        for sales in year2022[1:7]:
                sales2022 += int(sales)


    SGR = (sales2021 + sales2022) / sales2022

    text = str(SGR) + "\n"
    file.write(text)

    forcast=[]
    for month in year2021[7:]:
        forcast += [float(month) + float(month) * SGR]
    print(forcast)

    for sales in forcast:
        text = str(sales) + "\n"
        file.write(text)

    x = ['July', 'August', 'September', 'October', 'November', 'December']
    y = forcast

    plt.figure(1)
    plt.barh(x, y)

    plt.title("Forcast for 2022")
    plt.xlabel("Sales")
    plt.ylabel("Months")
    plt.grid()  # Showing grids on the plot

    plt.show()


    file.close()


