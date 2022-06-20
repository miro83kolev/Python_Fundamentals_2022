import sys

number_snowballs = int(input())
value=0
best_value = -sys.maxsize
message = ""

for each_snowball in range (1, number_snowballs+1):

    weight=int(input())
    time_needed=int(input())
    quality=int(input())

    value = int((weight/time_needed)**quality)
    if value>=best_value:
        best_value=value
        message = f"{weight} : {time_needed} = {best_value} ({quality})"
print(message)

