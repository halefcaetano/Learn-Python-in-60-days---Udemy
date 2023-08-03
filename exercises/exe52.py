def water_state(temperature):
    if temperature <= 0 :
        return "Solid"
    elif temperature > 0 and temperature < 100:
        return "Liquid"
    else:
        return "Gas"