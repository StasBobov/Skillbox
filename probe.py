height = 10
width = 7

full_str = '* ' * width
n_f_str = ('* ' * 2) + (' ' * 6) + ('* ' * 2)

for i in range(2):
    print(full_str)

for i in range(6):
    print(n_f_str)

for i in range(2):
    print(full_str)

'''__________________________________________________________'''


for i in range(5):
    print('* ' * (i +1))

'''__________________________________________________________'''

height = input('Введите высоту: ')

for i in range(int(height)):
    print(' ' * (int(height) - i - 1) + '* ' * (i+1))

'''__________________________________________________________'''


height = input('Введите высоту: ')
width = int(height) * 2 - 1
for row_counter in range(int(height)):
    left_part = width - (row_counter * 2 + 1)
    central_part = row_counter + 1
    print(left_part * ' ' + '* ' * central_part)

'''__________________________________________________________'''

dep = input('departure time: ')
trev = input('travel time: ')

dep_mins = (int(dep[:2]) * 60) + int(dep[3:])
trev_mins = (int(trev[:1]) * 60) + int(trev[2:])
ex_hours = (dep_mins + trev_mins) // 60
ex_mins = (dep_mins + trev_mins) % 60
print(f'{ex_hours}:{ex_mins}')

'''__________________________________________________________'''

time_24 = input('input time: ')

am_pm = None

time_hours = int(time_24[:2])
time_mins = int(time_24[3:])

if time_hours >= 12:
    time_hours -= 12
    am_pm = 'PM'
else:
    time_hours = int(time_24[1:2])
    am_pm = 'AM'

print(f'{time_hours}:{time_mins} {am_pm}')