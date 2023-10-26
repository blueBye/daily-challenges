from datetime import timedelta, datetime

current_time = datetime.strptime(input(), "%H:%M:%S")
alarm_time = datetime.strptime(input(), "%H:%M:%S")

delta = alarm_time - current_time
if alarm_time <= current_time:
    delta += timedelta(days = 1)

if delta.days:
    print('24:00:00')  # not specified

else:
    hours, remainder = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    print('{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds)))
