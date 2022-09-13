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