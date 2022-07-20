import csv

header = ['SNo', 'Hotel_name', 'Address', 'Price', 'Rating', 'Contact']

with open('delhi.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    for i in range(1, 3):
        print(i)
        i = i + 1
        hotel_name = input("hotel_name:")
        address = input("address:")
        price = int(input("price:"))
        rating = float(input("rating:"))
        contact = int(input("contact:"))

        n = i - 1

        data = [n, hotel_name, address, price, rating, contact]

        # write the data
        writer.writerow(data)
