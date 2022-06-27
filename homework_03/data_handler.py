import json

from csv import reader

with open('users.json', 'r') as users:
    users_data = json.load(users)

with open('books.csv', newline='') as books:
    books_list = reader(books)
    headers = next(books_list)
    books_data = []
    for row in books_list:
        books_data.append(dict(zip(headers[:4], row[:4])))

for_one = len(books_data) // len(users_data)
ost = len(books_data) % len(users_data)

data = []
i = 0
for user in users_data:
    data.append({'Name': user['name'],
                 'Gender': user['gender'],
                 'Address': user['address'],
                 'Age': user['age'],
                 'Books': books_data[for_one * i:for_one * (i + 1)]})
    i += 1

for i in range(ost):
    data[i]['Books'].append(books_data[len(books_data) - (i + 1)])

with open('result.json', 'w') as result:
    json.dump(data, result, indent=4)
