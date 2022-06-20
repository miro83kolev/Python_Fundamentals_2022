# all_fires = input().split("#")
# water=int(input())
# total_effort=0
#
# fire_list = []
#
# for fire in all_fires:
#     temp_event=fire.split("=")
#     level=temp_event[0]
#     cell=int(temp_event[1])
#     if level=="High" and not 1<= cell => 125:
#         continue
#     if level=="Medium" and not cell >80:
#         continue
#     if level=="Low" and not cell >50:
#         continue
#     if water<cell:
#         continue
#     water -=cell
#     fire_list.append(cell)
#     total_effort +=cell*0.25
# print("Cells:")
# for el in fire_list:
#     print(f"- {str(el)}")
# print(f"Effort: {total_effort:.2f}")
# print(f"Total fire: {str(sum(fire_list))}")

fires_cells = input().split("#")
water = int(input())
effort = 0
total_fire = []
for i in range(len(fires_cells)):
    level, cell = fires_cells[i].split(" = ")
    cell = int(cell)
    if level == "Low" and not 1 <= cell <= 50:#if level == "Low" and cell > 50:
        continue
    if level == "Medium" and not 51 <= cell <= 80:
        continue
    if level == "High" and not 81 <= cell <= 125:
        continue
    if water < cell:
        continue
    water -= cell
    total_fire.append(cell)
    effort += cell * 0.25
print("Cells:")
for el in total_fire:
    print(f" - {str(el)}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {str(sum(total_fire))}")







