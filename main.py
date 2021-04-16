
Driver_speed = int(input("Current speed: "))
Average_speed = int(input("Average speed allowed: "))
points = (Driver_speed - Average_speed) / 5
if Driver_speed < 60:
    print("Ok")
else:
    if points >= 12:
        print("demerit points: " + str(points))
    else:
        print("time to go to jail")