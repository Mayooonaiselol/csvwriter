import csv

header = ['SNo', 'Hotel_name', 'Address', 'Price', 'Rating', 'Contact'] # Change the Column headings here.

with open('delhi.csv', 'w', encoding='UTF8') as f: # Enter filename
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    for i in range(1, 3):
        print(i)
        i = i + 1

        # Change the input fields here
        hotel_name = input("hotel_name:")
        address = input("address:")
        price = int(input("price:"))
        rating = float(input("rating:"))
        contact = int(input("contact:"))

        n = i - 1

        data = [n, hotel_name, address, price, rating, contact] # writing in the file

        # write the data
        writer.writerow(data)
