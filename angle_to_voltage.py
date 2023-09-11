def angle_to_voltage(angle1,angle2):
    #if 0<angle1<=30:
    #    angle1=0
    #elif 30<angle1<=60:
    #    angle1=1
    #elif 60<angle1<=90:
    #    angle1=2
    interval_size1 = 90 / 3

    interval_size2 = 360 / 12

    num1 = angle1 // interval_size1

    num2 = angle2 // interval_size2

    if num1 > 3:
        num1 = 3.0
    elif num1 < 0:
        num1 = 0.0
    if num2 > 12:
        num2 = 12.0
    elif num2 < 0:
        num2 = 0.0


    return num1, num2


