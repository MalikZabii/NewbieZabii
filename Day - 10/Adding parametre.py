year = int(input("Which Year Do You Want To Check?"))


def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return "It is a leap Year"
            else:
                return "Not Leap Year"
        else:
            return "Leap Year"
    else:
        return "Not Leap Year"


print(leap_year(year))
