def comparador(pot1, pot2, azimuth, elevacion):
    if pot1 < azimuth:
        IN1 = 1
        IN2 = 0
    elif pot1 > azimuth:
        IN1 = 0
        IN2 = 1
    else:
        IN1 = 0
        IN2 = 0
    if pot2 < elevacion:
        IN3 = 1
        IN4 = 0
    elif pot2 > elevacion:
        IN3 = 0
        IN4 = 1
    else:
        IN3 = 0
        IN4 = 0
    return IN1, IN2, IN3, IN4
