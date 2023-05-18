# Посчитайте количество согласных букв в данной строке.

text = ...
text="аа б я"

soglasnue=["Б", "В", "Г", "Д", "Ж", "З", "Й", "К", "Л", "М", "Н", "П", "Р", "С", "Т", "Ф", "Х", "Ц", "Ч", "Ш", "Щ"]
count=0
for world in text.upper():
    if world in soglasnue:
        count+=1
print(count)
