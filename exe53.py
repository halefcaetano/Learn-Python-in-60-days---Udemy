def water_state(temperature):
    FREEZING_POINT = 0
    BOILING_POINT = 100
    if temperature <= FREEZING_POINT:
        return "Solid"
    elif temperature > FREEZING_POINT and temperature < BOILING_POINT:
        return "Liquid"
    else:
        return "Gas"