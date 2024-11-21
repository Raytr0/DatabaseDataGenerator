import csv
import random
import string

with open('users.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["customerId", "address", "emailAddress", "phoneNumber"]

    writer.writerow(field)

    for i in range(1491):
        phoneNumber = ''.join(random.choices(string.digits, k=9))
        password = ''.join(random.choices(string.ascii_lowercase +
                                     string.ascii_uppercase + string.digits, k=N))
        writer.writerow(["", address, emailAddress, phoneNumber])
