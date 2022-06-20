year = int(input())
is_year_happy = False

while not is_year_happy:
    year +=1
    str_year = str(year)
    set_year= set()
    for i in range (len(str_year)):
        set_year.add(str_year[i])

    if len(str_year)==len(set_year):
        is_year_happy = True

print(year)

# year = int(input())
# is_year_happy = False
#
# while not is_year_happy:
#     year +=1
#     str_year = str(year)
#     set_year= set(str_year)
#
#     if len(str_year)==len(set_year):
#         is_year_happy = True
#
# print(year)
