# Necessary imports to request the website and scrape it
from bs4 import BeautifulSoup
import requests
import sys

# Pull the HTML of the site, and then scrape only the table with the years and percentage changes
soup = BeautifulSoup(requests.get("https://www.fool.com/investing/how-to-invest/index-funds/average-return/").content, "html5lib")
data = soup.find_all("td")[0:60]

# Cleans up the data by getting just the raw text and removing
# the '%' symbol if necessary
i = 0
for element in data:
    if i % 2 == 1:
        data[i] = element.getText()[0:len(element.getText())-1]
    else:
        data[i] = element.getText()
    i = i + 1

# Prints a notice to the user
print("/----------------------------------\\")
print("|          /!\\ NOTICE /!\\          |")
print("|  This is a lump sum calculator.  |")
print("| This is only to see how much you |")
print("| would've made had you invested a |")
print("| certain amount at the start of a |")
print("|  certain year into the S&P 500.  |")
print("|                                  |")
print("|   This cannot tabulate monthly   |")
print("|  investments with montly yeilds  |")
print("|   as it assumes you invest one   |")
print("|   time and leave it until your   |")
print("|   previously chosen ROI Date.    |")
print("\\----------------------------------/")
print()

# Ensures that the program receives an accurate start and end year
startYear = 0
while (startYear < 1991 or startYear > 2019):
    startYear = int(input("Please input a start year (1991 - 2019): "))

endYear = 0
while (endYear < startYear + 1 or endYear > 2020):
    endYear = int(input("Please input an end year (" + str(startYear + 1) + " - 2020): "))

initialInvestment = int(input("How much money would you like to invest? "))
total = initialInvestment

# This segment does some math to figure out the ROI and the indexs in data
totalInvestedYears = endYear - startYear
startIndex = (startYear - 1991)*2
endIndex = (endYear - 1991)*2

# Prints a report of the initial investment, and what the total is at the end of every year.
print()
print()
print("Initial Investment: $" + str("{:,.2f}".format(initialInvestment)))
print()

while(startIndex <= endIndex):
    total = total + ((float(data[startIndex + 1])/100) * total)
    print("End of " + data[startIndex] + ": $" + str("{:,.2f}".format(total)))
    startIndex = startIndex + 2

# Prints a final report showing the total amount in the account, how much of it is
# profit, and what the ROI is.
print()
print("Total Amount: $" + str("{:,.2f}".format(total)))
print("Total Profit: $" + str("{:,.2f}".format(total - initialInvestment)))
print("Return on Investment: " + str(totalInvestedYears) + " years.")