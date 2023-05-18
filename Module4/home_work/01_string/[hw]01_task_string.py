# Дан произвольный текст. Каких символов больше, точек "." или запятых ","?
# Если точек и запятых одинаково - выведите "одинаково"
str=(input("str= "))


count_t=str.count(".")
count_z=str.count(",")

if count_t>count_z:
    print("точек больше")
elif count_z>count_t:
    print("запятых больше")
elif count_z==0 and  count_t==0:
    print("точка и запятая отсутствуют")
else:
    print("одинаково")
text = ...
