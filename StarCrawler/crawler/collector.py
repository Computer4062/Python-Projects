import os
import pandas as pd

file = open('output.txt', 'w')
text = file.write(" ")
file.close()

os.system('scrapy crawl crawler')

file = open('output.txt', 'r')
text = file.readlines()
file.close()

names = []
text2 = []
for item in text:
    count = -1
    for letter in item:
        count += 1
        if letter == '|':
            name = item[:count]
            names.append(name)

            all_item = item[count + 1:]
            text2.append(all_item)

            break

print(text2)

prices = []
text3 = []
for item in text2:
    count = -1
    for letter in item:
        count += 1
        if letter == '|':
            price = item[:count]
            prices.append(price)

            all_item = item[count + 1:]
            text3.append(all_item)

            break

availability = []

for item in text3:
    part = item[:-1]
    availability.append(part)


data = {
    "Name": names,
    "Price": prices,
    "Availability": availability
}

os.system('cls')

table = pd.DataFrame(data)
print(table)

input()





