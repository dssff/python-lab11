import csv

input_file = 'lab11.csv'
output_file = 'output_file.csv'

min_value = float('inf')
max_value = float('-inf')
min_row = None
max_row = None
with open('lab11.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    
    # Печатаем каждую строку
    for row in reader:
        print(row)

with open(input_file, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    headers = next(reader)  
    for row in reader:
 
        if row and row[-1]:  
            try:
                value = float(row[-1])
                if value < min_value:
                    min_value = value
                    min_row = row
                if value > max_value:
                    max_value = value
                    max_row = row
            except ValueError:

                continue

with open(output_file, 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers) 
    if min_row:
        writer.writerow(['Мінімальне значення'] + min_row)
    if max_row:
        writer.writerow(['Максимальне значення'] + max_row)

print(f"Мінімальне значення: {min_value} записано в {output_file}")
print(f"Максимальне значення: {max_value} записано в {output_file}")
