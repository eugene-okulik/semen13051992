from datetime import datetime

data = "Jan 15, 2023 - 12:05:33"

python_date = datetime.strptime(data, '%b %d, %Y - %H:%M:%S')
month = python_date.strftime('%B')
new_data = python_date.strftime('%d.%m.%Y, %H:%M')

print(python_date)
print(month)
print(new_data)
