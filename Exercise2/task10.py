from time import gmtime, strftime


def clock():
    alarm_time = input("Enter alarm time (00: 00: 00 AM/PM): ")
    time = ''
    while True:
        if alarm_time != time:
            time = strftime('%H: %M: %S %p')
            print(time)
        else:
            print('WAKE UP!')
            break

clock()

