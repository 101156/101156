#Задание 1
the_minimum_number_of_instructions = 0
x = int(input())
y = int(input())
x1 = 0
y1 = 0
z = 'север'
direction_of_movement = input()
while direction_of_movement != 'стоп':
    if int(x) == x1 and int(y) == y1:
        print(the_minimum_number_of_instructions)
        print(z)
        break
    else:
        the_minimum_number_of_instructions += 1
        if direction_of_movement == 'вперёд':
            steps = int(input())
            if z == 'север':
                y1 += steps
            elif z == 'запад':
                x1 -= steps
            elif z == 'юг':
                y1 -= steps
            elif z == 'восток':
                x1 += steps
        elif direction_of_movement == 'направо':
            if z == 'север':
                z = 'восток'
            elif z == 'восток':
                z = 'юг'
            elif z == 'юг':
                z = 'запад'
            elif z == 'запад':
                z = 'север'
        elif direction_of_movement == 'налево':
            if z == 'север':
                z = 'запад'
            elif z == 'запад':
                z = 'юг'
            elif z == 'юг':
                z = 'восток'
            elif z == 'восток':
                z = 'север'
        elif direction_of_movement == 'разворот':
            if z == 'север':
                z = 'юг'
            elif z == 'юг':
                z = 'север'
            elif z == 'запад':
                z = 'восток'
            elif z == 'восток':
                z = 'запад'
        if int(x) == x1 and int(y) == y1:
            print(the_minimum_number_of_instructions)
            print(z)
            break
        direction_of_movement = input()
else:
    if x == 0 and y == 0:
        print(0)
        print("север")

#Задание 2
d = int(input())
m = int(input())
y = int(input()) 
y = y if (m - 2) > 0 else y - 1
m = m - 2 if (m - 2) > 0 else 12 - abs(m - 2) 
c = y // 100 
y = y % 100
n = (d + ((13 * m - 1) // 5) + y + (y // 4 + c // 4 - 2 * c + 777)) % 7
print(n)

#Задание 3
s = input()
print(s[2])
print(s[-2])
print(s[:5])
print(s[:-2])
print(s[::2])
print(s[1::2])
print(s[::-1])
print(s[::-2])
print(len(s))