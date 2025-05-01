x = 1
y = -1

# TODO переписать через if-elif-else
if x > 0:
    if y > 0:
        print("Первая четверть")
    elif y < 0:
        print ("Четвертая четверть")
else:
    if y > 0:
        print ("Вторая четверть")
    elif y < 0:
        print("Третья четверть")

if x == 0 and y == 0:
    print ("Числа не могут быть равны 0")