# Replace the "ANSWER HERE" for your answer
def is_leap_year(year : int) -> bool:
    if year < 100:
        if year % 4 == 0:
            print(f"El año {year} es bisiesto")
            return True
    else:
        if year % 400 == 0:
            print(f"El año {year} es bisiesto")
            return True
    print(f"El año {year} no es bisiesto")
    return False
