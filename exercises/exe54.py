def temp(parameter):
    if parameter > 25:
        return "Hot"
    elif parameter >= 15 and parameter <= 25:
        return "Warm"
    else:
        return "Cold"