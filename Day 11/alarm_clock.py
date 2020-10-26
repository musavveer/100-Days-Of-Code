import datetime

alarmHour = int(input("Enter Hour: "))
alarmMinute = int(input("Enter Minute: "))
AmPm = str(input("am or pm: "))

print("Waiting for alarm", alarmHour,":", alarmMinute, AmPm)

if(AmPm == "pm"):
    alarmHour = alarmHour + 12

while(1 == 1):
    if(alarmHour == datetime.datetime.now().hour and alarmMinute == datetime.datetime.now().minute):
        print("Time To Wake UP!!!")
        break