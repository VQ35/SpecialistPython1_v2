# Дано 3 кортежа заполненные произвольными целыми числами.
# Найдите количество элементов, которые встречаются во всех трех кортежах.
tup1 = (1, 2, 3,4,5)
tup2 = (2, 3,10,1)
tup3 = (1,2,3)

qty=0
for i1 in tup1:
    for i2 in tup2:
        for i3 in tup3:
            if i1==i2 and i2==i3:
                qty+=1
print(qty)
# TODO: your code here
